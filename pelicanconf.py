#!/usr/bin/env python
# -*- coding: utf-8 -*- #
"""Settings for Pelican Blog: andrewtcrooks.com."""

AUTHOR = u'Andrew T. Crooks'
SITENAME = u'Andrew T. Crooks'
SITEURL = 'http://www.andrewtcrooks.com'
TIMEZONE = 'US/Pacific'
THEME = 'void/'
TITLE = "Example: What is the title of your site?"    								# EDIT THIS
DESCRIPTION = "Python programming blog."			# EDIT THIS

HEAD_IMAGE = '/images/headshot.jpg'
LOGO_IMAGE = '/images/dsd-logo_color.svg'
FAVICON_IMAGE = '/images/dsd-logo_color-dark.svg'

ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

DIRECT_TEMPLATES = ('404', 'analytics', 'article', 'base', 'blog',
                    'footer', 'index', 'navbar', 'page', 'sitemap',
                    'tag')
SITEMAP_SAVE_AS = 'sitemap.xml'


# Static Pages
PAGE_PATHS = ['pages']
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
ABOUT_PAGE_HEADER = 'About'


# DEFAULTS
DEFAULT_LANG = 'en'
DEFAULT_CATEGORY = 'misc'
DEFAULT_DATE = 'fs'
DEFAULT_DATE_FORMAT = '%b %d, %Y'
DEFAULT_PAGINATION = False

# FEEDS
FEED_ALL_ATOM = "feeds/all.atom.xml"
TAG_FEED_ATOM = "feeds/tag/%s.atom.xml"

MARKUP = ('md', 'ipynb')

# PLUGINS
PLUGIN_PATHS = ['pelican-plugins', 'pelican_dynamic']
PLUGINS = ['assets', 'pelican-ipynb.liquid', 'pelican_dynamic']

CODE_DIR = 'code'
# NOTEBOOK_DIR = 'notebooks'
STATIC_PATHS = ['2017', 'images', 'code', 'notebooks', 'extra', 'data']
EXTRA_PATH_METADATA = {'extra/robots.txt': {'path': 'robots.txt'}, }

NAVIGATION = [
    # You probably want to fill these in so they point to your user pages
    {
        'site': 'twitter',
        'user': '',
        'url': 'https://twitter.com/andrewtcrooks'
    },
    {
        'site': 'github',
        'user': '',
        'url': 'https://github.com/andrewtcrooks'
    },
    {
        'site': 'linkedin',
        'user': '',
        'url': 'http://linkedin.com/in/andrewtcrooks'
    },

    # {
    #     'site': 'twitter',
    #     'user': '',
    #     'url': 'http://www.kaggle.com/darkstardata'
    # },
    # {
    #     'site': 'google-plus',
    #     'user': '',
    #     'url': 'https://plus.google.com/...'
    # },
    # {
    #     'site': 'spotify',
    #     'user': '',
    #     'url': 'https://open.spotify.com/user/...'
    # },
]

# TODO
# TWITTER_NAME = ""
# TWITTER_CARDS = True
# FACEBOOK_SHARE = True
# HACKER_NEWS_SHARE = True


# Analytics
GOOGLE_ANALYTICS = 'UA-99294612-1'
# DOMAIN = "http://www.andrewtcrooks.com"


# Other
CACHE_CONTENT = False

COPYRIGHT_START_YEAR = 2017

IGNORE_FILES = ['.ipynb_checkpoints', 'page_examples']

EXTRA_HEADER = open('_nb_header.html').read()

LOAD_CONTENT_CACHE = False
