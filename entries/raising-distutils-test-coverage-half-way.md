Title: Raising Distutils test coverage : half-way 
Date: 2009-02-23 13:06
Category: distutils, python, quality

After the next commit I will make in Distutils (that adds tests for
bdist\_rpm), the test coverage of this Python standard library package
will be at 41%. This means that I have doubled the test coverage over
the past few months, from **18% to 41%**.   
  
My goal is to double it again, and reach 80% in the next 6 months.   
  
This also means I am just half an idiot now ! (since [people who don't
have 100% code coverage are idiots][] ;)).   
  
So does it make Distutils more robust ?   
  
It would have probably made the latest Python 3 release looks better
for this package, since we had a [uncovered cmp() call left in
Distutils][] by the time the release was made. In the meantime, [as I
said before][], the "real" Distutils regression test suite is held by
all the packages out there in the community, that are built and
installed everyday.   
  
**Python trunk Distutils test coverage : 41%   
**   
   Name               Stmts   Exec  Cover

    --------------------------------------

    __init__               3      0     0%

    archive_util          77     61    79%

    bcppcompiler         185      0     0%

    ccompiler            453    211    46%

    cmd                  180    134    74%

    config                73     59    80%

    core                  93     50    53%

    cygwinccompiler      161      0     0%

    debug                  3      3   100%

    dep_util              43     11    25%

    dir_util             109     76    69%

    dist                 581    386    66%

    emxccompiler         118      0     0%

    errors                49      0     0%

    extension             97     28    28%

    fancy_getopt         233    126    54%

    file_util            124     77    62%

    filelist             161    102    63%

    log                   46     21    45%

    msvc9compiler        408      0     0%

    msvccompiler         370      0     0%

    spawn                 93     28    30%

    sysconfig            323     51    15%

    text_file            112     61    54%

    unixccompiler        160     64    40%

    util                 255    157    61%

    version               68     62    91%

    versionpredicate      61     51    83%

    __init__               3      3   100%

    bdist                 61     35    57%

    bdist_dumb            57     47    82%

    bdist_msi            322      0     0%

    bdist_rpm            252    198    78%

    bdist_wininst        170      0     0%

    build                 60     54    90%

    build_clib            90      0     0%

    build_ext            334    160    47%

    build_py             213    178    83%

    build_scripts         78     65    83%

    clean                 35      0     0%

    config               185      0     0%

    install              251    156    62%

    install_data          44      0     0%

    install_egg_info      40     32    80%

    install_headers       25      0     0%

    install_lib           97     50    51%

    install_scripts       33     29    87%

    register             173     82    47%

    sdist                228    180    78%

    upload               112     38    33%

    --------------------------------------

    TOTAL               7502   3126    41%

  
**   
Python 2.5.4 Distutils test coverage : 18%**   
   Name               Stmts   Exec  Cover

    --------------------------------------

    __init__               3      0     0%

    archive_util          78     11    14%

    bcppcompiler         185      0     0%

    ccompiler            453      0     0%

    cmd                  180     79    43%

    core                  93     15    16%

    cygwinccompiler      160      0     0%

    debug                  3      3   100%

    dep_util              43      4     9%

    dir_util             106     50    47%

    dist                 578    342    59%

    emxccompiler         118      0     0%

    errors                49      0     0%

    extension             97      9     9%

    fancy_getopt         233    121    51%

    file_util            121     50    41%

    filelist             162      0     0%

    log                   46     15    32%

    msvccompiler         365      0     0%

    mwerkscompiler       140      0     0%

    spawn                 93      0     0%

    sysconfig            296     10     3%

    text_file            146      0     0%

    unixccompiler        159      0     0%

    util                 235     69    29%

    version               68     48    70%

    versionpredicate      61     51    83%

    __init__               3      3   100%

    bdist                 59      0     0%

    bdist_dumb            57      0     0%

    bdist_msi            320      0     0%

    bdist_rpm            248      0     0%

    bdist_wininst        159      0     0%

    build                 52     47    90%

    build_clib            90      0     0%

    build_ext            304      0     0%

    build_py             213    143    67%

    build_scripts         78     64    82%

    clean                 35      0     0%

    config               185      0     0%

    install              220    120    54%

    install_data          44      0     0%

    install_egg_info      40      0     0%

    install_headers       26      0     0%

    install_lib           96      0     0%

    install_scripts       33     29    87%

    register             171      0     0%

    sdist                204      0     0%

    upload               118      0     0%

    --------------------------------------

    TOTAL               7026   1283    18%

  [people who don't have 100% code coverage are idiots]: http://ivory.idyll.org/blog/feb-09/people-who-dont-use-code-coverage-are-idiots
  [uncovered cmp() call left in Distutils]: http://mail.python.org/pipermail/python-dev/2009-February/086156.html
  [as I said before]: http://tarekziade.wordpress.com/2009/02/08/a-distutils-regression-test-system/
