# -*- coding: utf-8 -*-
AUTHOR = u'Tarek Ziadé'
SITENAME = u"Fetchez le Python"
SITESUBTITLE = AUTHOR
SITEURL = 'http://blog.ziade.org'
TIMEZONE = "Europe/Paris"
CLEAN_URLS = True
GITHUB_URL = 'http://github.com/tarekziade/'
DISQUS_SITENAME = "fetchezlepython"
PDF_GENERATOR = False
REVERSE_CATEGORY_ORDER = True
LOCALE = ""
DEFAULT_PAGINATION = 10
PATH = 'entries'
OUTPUT_PATH = 'html'
FEED_RSS = 'feed'
CATEGORY_FEED_RSS = 'category/%s/feed'
ARTICLE_PERMALINK_STRUCTURE = '/%Y/%m/%d'
MENUITEMS = [('Home', 'http://blog.ziade.org'),
             ('Books', 'books'),
             ('Resume', 'resume'),
             ('Contact me', 'contact')]
THEME = 'theme'

STATIC_PAGES = {'/books': 'static/books.html',
                '/resume': 'static/resume.html',
                '/contact': 'static/contact.html'}
