Title: Protecting a Python svn code base with the pre-commit hook
Date: 2006-11-01 12:29
Category: python, quality

In a community project, opened to various contributors, there are a few
thing to take care of in order not to break the code. I am not talking
about code reviewing but about bad code editing that breaks it all.   
  
Most frequent errors are:   
-   **<tab\> insertions**, that get mixed with space-based indentation
-   **carriage return insertion**, before line feeds with some weird
    windows editors

  
Instead of tracking the developers that commited such things, and send
them an army of white rabbits, an automatic code check is way better. It
is not a good idea though, to clean up incoming code. The best thing to
do is to block unwanted changes and warn the commiters, so they learn
about it.   
  
This is really easy with Subversion. I have grabbed a script on the
web, and adapted it a bit for this task. Here it is:   
   #!/usr/bin/python2.4

    # -*- coding: UTF-8 -*-

    # adapted from:

    #   http://blog.wordaligned.org/articles/2006/08/09/a-subversion-pre-commit-hook

    # by Tarek Ziadé 



    from subprocess import Popen

    from subprocess import PIPE

    import re

    import os



    re_options = re.IGNORECASE | re.MULTILINE | re.DOTALL



    class EOF(object):

        def findall(self, content):

            if content.endswith('\\n'):

                return []

            return ['\n']



    tab_catcher = re.compile(r'^\\t', re_options)

    windows_catcher = re.compile(r'\\r\\n$', re_options)



    testers = (('found TAB', tab_catcher),

               ('found CR/LF', windows_catcher),

               ('no new line at the end', EOF()))



    def command_output(cmd):

        """ Capture a command's standard output."""

        return Popen(cmd.split(), stdout=PIPE).communicate()[0]



    def files_changed(look_cmd):

        """ List the files added or updated by this transaction."""

        def filename(line):

            return line[4:]



        def added_or_updated(line):

            return line and line[0] in ("A", "U")



        return [filename(line) for line in

                command_output(look_cmd % "changed").split("n")

                if added_or_updated(line)]



    def file_contents(filename, look_cmd):

        """Return a file's contents for this transaction"""

        return command_output("%s %s" % (look_cmd % "cat", filename))



    def test_expression(expr, filename, look_cmd):

        """test regexpr over file"""

        return len(expr.findall(file_contents(filename, look_cmd))) > 0



    def check_file(look_cmd):

        """checks Python files in this transaction"""

        def is_python_file(fname):

            return os.path.splitext(fname)[1] in ".py".split()



        erroneous_files = []



        for file in files_changed(look_cmd):

            if not is_python_file(file):

                continue



            for error_type, tester in testers:

                if test_expression(tester, file, look_cmd):

                    erroneous_files.append((error_type, file))



        num_failures = len(erroneous_files)



        if num_failures > 0:

            sys.stderr.write("[ERROR] please check your files:n")

            for error_type, file in erroneous_files:

                sys.stderr.write("[ERROR] %s in %sn" % (error_type, file))



        return num_failures



    def main():

        from optparse import OptionParser

        parser = OptionParser()

        parser.add_option("-r", "--revision",

                            help="Test mode. TXN actually refers to a revision.",

                            action="store_true", default=False)

        errors = 0

        (opts, (repos, txn_or_rvn)) = parser.parse_args()

        look_opt = ("--transaction", "--revision")[opts.revision]

        look_cmd = "svnlook %s %s %s %s" % (

            "%s", repos, look_opt, txn_or_rvn)

        errors += check_file(look_cmd)



        return errors



    if __name__ == "__main__":

        import sys

        sys.exit(main())

  
I've also added a *new line at end of file* control. This script has to
be called in the* pre-commit hook* script (look up in SVN documentation)
  
  
The call should look like:   
   /chemin/vers/script/svn_check_source.py "$REPOS" "$TXN" || exit 1

  
You can then extend the controls made by this script, by controlling
for example the quality of the commited code with tools like
[pychecker][]. But these extra controls should not block commits and
should be quite light to perform because the commiter waits for the
changeset to be validated.   
  
Sending a mail to the commiter with suggestions when her code doesn't
pass some quality checks is a better idea. Furthermore, for an extensive
QA test, it is simpler to hook a script on a system like [buildbot][]
and create a nighlty digest over the whole code base. [Pylint][] is very
handy on this kind of controls, and can be fine tuned to generate a
useful QA report that buildbot can send to developers.

  [pychecker]: http://pychecker.sourceforge.net/
  [buildbot]: http://buildbot.sourceforge.net/ "Buildbot"
  [Pylint]: http://www.logilab.org/projects/pylint "PyLint"
