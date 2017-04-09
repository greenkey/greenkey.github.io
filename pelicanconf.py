#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'greenkey'
SITENAME = 'loman.it'
SITESUBTITLE = 'home of Lorenzo Mele'
SITELOGO = 'https://pbs.twimg.com/profile_images/664404104836489216/6bN2VkLF_400x400.jpg'

PATH = 'content'
THEME = 'theme/Flex'

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
CUSTOM_CSS = 'static/loman.css'
STATIC_PATHS = [CUSTOM_CSS]
EXTRA_PATH_METADATA = {
    CUSTOM_CSS: {'path': CUSTOM_CSS}
}

# Social widget
SOCIAL_WIDGET_NAME = 'Find me here'
SOCIAL = (
	('twitter', 'http://twitter.com/greenkey'),
	('linkedin', 'http://linkedin.com/in/lorenzomele'),
	('github', 'http://github.com/greenkey'),
	('devto', 'https://dev.to/greenkey'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
