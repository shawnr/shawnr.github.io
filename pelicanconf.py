#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Shawn Rider'
SITENAME = u'@shawnr codes'
SITETITLE = u'@shawnr codes'
SITEURL = 'http://localhost:8000'

THEME = "Flex"
SITELOGO = '/images/shawnr.jpg'
PYGMENTS_STYLE = 'monokai'

PATH = 'content'
STATIC_PATHS = ['images', 'extra/CNAME', 'extra/favicon.ico']
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
}

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Portfolio', 'http://shawnrider.com/'),
         ('SU Webdev', 'http://webdev.seattleu.edu/'),)

# Social widget
SOCIAL = (('github', 'https://github.com/shawnr'),
          ('twitter', 'https://twitter.com/shawnr'),
          ('linkedin', 'https://www.linkedin.com/in/shawnrider/'),
          ('rss', 'feeds/all.atom.xml'),)

MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)

DEFAULT_PAGINATION = 10

ROBOTS = 'index, follow'

CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '4.0',
    'slug': 'by-sa'
}

COPYRIGHT_YEAR = 2017

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
