# -*- coding: utf-8 -*-
AUTHOR = u'Tarek Ziadé'
SITENAME = u"Fetchez le Python"
SITEURL = 'http://blog.ziade.org'
TIMEZONE = "Europe/Paris"
CLEAN_URLS = True
GITHUB_URL = 'http://github.com/tarekziade/'
DISQUS_SITENAME = "blog-tarekziade"
PDF_GENERATOR = False
REVERSE_CATEGORY_ORDER = True
LOCALE = ""
DEFAULT_PAGINATION = 10
PATH = 'entries'
OUTPUT_PATH = 'html'
FEED_RSS = 'feed.xml'
CATEGORY_FEED_RSS = 'category/%s/feed.xml'
ARTICLE_PERMALINK_STRUCTURE = '/%Y/%m/%d'
MENUITEMS = [('Home', 'http://ziade.org'),
             ('Blog', 'http://blog.ziade.org'),
             ('Books', 'http://ziade.org/books'),
             ('Resume', 'http://ziade.org/resume'),
             ('Contact me', 'http://ziade.org/contact')]
THEME = 'theme'
