#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'greenkey'
SITENAME = 'loman.it'
SITESUBTITLE = 'home of Lorenzo Mele'
SITEURL = '/'

PATH = 'content'
THEME = 'theme/Flex'
INDEX_SAVE_AS = 'articles.html'

TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
PAGES_SORT_ATTRIBUTE = 'sortorder'
SHOW_ARCHIVES = False
DIRECT_TEMPLATES = []

# Social widget
SOCIAL_WIDGET_NAME = 'Find me here'
SOCIAL = (
	('twitter', 'http://twitter.com/greenkey'),
	('linkedin', 'http://linkedin.com/in/lorenzomele'),
	('github', 'http://github.com/greenkey'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
