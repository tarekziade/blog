# -*- coding: utf-8 -*-
AUTHOR = "Tarek Ziadé"
SITENAME = "Fetchez le Python"
SITESUBTITLE = AUTHOR
SITEURL = "https://ziade.org"
TIMEZONE = "Europe/Paris"
GITHUB_URL = "http://github.com/tarekziade/"
# DISQUS_SITENAME = "fetchezlepython"
PDF_GENERATOR = False
REVERSE_CATEGORY_ORDER = True
LOCALE = ""
DEFAULT_PAGINATION = 10
PATH = "entries"
OUTPUT_PATH = "html"
FEED_RSS = "feed"
TAG_FEED_RSS = "tag/%s/feed"
CATEGORY_FEED_RSS = "category/%s/feed"
MENUITEMS = [("Home", "/"), ("Books", "/books.html"), ("About Me", "/resume.html")]
THEME = "theme"

THEME_TEMPLATES_OVERRIDES = ["static"]
TEMPLATE_PAGES = {"books.html": "books.html", "resume.html": "resume.html"}

ARTICLE_URL = "{slug}/"
ARTICLE_LANG_URL = "{slug}-{lang}/"
PAGE_URL = "pages/{slug}/"
PAGE_LANG_URL = "pages/{slug}-{lang}/"

ARTICLE_URL = "{date:%Y}/{date:%m}/{date:%d}/{slug}/"
ARTICLE_LANG_URL = "{date:%Y}/{date:%m}/{date:%d}/{slug}-{lang}/"
PAGE_URL = "{date:%Y}/{date:%m}/{date:%d}/pages/{slug}/"
PAGE_LANG_URL = "{date:%Y}/{date:%m}/{date:%d}/pages/{slug}-{lang}/"
ARTICLE_SAVE_AS = "{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html"
ARTICLE_LANG_SAVE_AS = "{date:%Y}/{date:%m}/{date:%d}/{slug}-{lang}/index.html"
PAGE_SAVE_AS = "{date:%Y}/{date:%m}/{date:%d}/pages/{slug}/index.html"
PAGE_LANG_SAVE_AS = "{date:%Y}/{date:%m}/{date:%d}/pages/{slug}-{lang}/index.html"

MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.codehilite": {"css_class": "highlight"},
        "markdown.extensions.abbr": {},
        "markdown.extensions.footnotes": {},
        "markdown.extensions.tables": {},
        "markdown.extensions.toc": {},
        "markdown.extensions.fenced_code": {},
    }
}
