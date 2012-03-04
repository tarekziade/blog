Title: Syntastic now with Flake8
Date: 2011-12-04 22:36
Category: mozilla, python

If you're a VIM user and a Python coder, that could interest you.   
  
[Syntastic][], a syntax checker for VIM now includes [Flake8][] as a
checker for Python code.   
  
Syntastic can be used to check for syntax errors in files opened in
VIM. It has a pretty extensive list of supported languages.   
  
For Python it had PyFlakes, and since the latest version, it has my
small glue script "Flake8", that reunites in a single stream: pep8,
PyFlakes and a McCabe checker.   
  
For Flake8 the next step is to support Python 3 -- as soon as I find
some time, or a volunteer ;)   
  
Thanks to *Sylvain Soliman* (and Clayton Parker) !

  [Syntastic]: http://www.vim.org/scripts/script.php?script_id=2736
  [Flake8]: http://pypi.python.org/pypi/flake8
