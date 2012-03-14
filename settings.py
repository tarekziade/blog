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
TAG_FEED_RSS  = 'tag/%s/feed'
CATEGORY_FEED_RSS = 'category/%s/feed'
ARTICLE_PERMALINK_STRUCTURE = '/%Y/%m/%d/'
MENUITEMS = [('Home', '/'),
             ('Books', '/books.html'),
             ('Resume', '/resume.html'),
             ('Contact me', '/contact.html'),
             ('Tools', '/tools.html')]
THEME = 'theme'

STATIC_PAGES = {'/books.html': 'static/books.html',
                '/resume.html': 'static/resume.html',
                '/contact.html': 'static/contact.html',
                '/tools.html': 'static/tools.html'}
