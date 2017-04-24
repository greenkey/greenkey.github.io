#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# site metadata
AUTHOR = 'Lorenzo Mele'
SITENAME = 'loman.it'
SITESUBTITLE = 'home of Lorenzo Mele'
SITELOGO = 'https://pbs.twimg.com/profile_images/664404104836489216/' + \
    '6bN2VkLF_400x400.jpg'

# config
TIMEZONE = 'Europe/Rome'
DEFAULT_LANG = 'en'

# content
PATH = 'content'
RELATIVE_URLS = True
DEFAULT_CATEGORY = 'blog'

# theme, templates, style
THEME = 'theme/Flex'
DIRECT_TEMPLATES = ['index', 'tags', 'archives']
EXTRA_TEMPLATES_PATHS = ['theme']
CUSTOM_CSS = 'static/loman.css'
STATIC_PATHS = [CUSTOM_CSS]
EXTRA_PATH_METADATA = {
    CUSTOM_CSS: {'path': CUSTOM_CSS}
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
PAGES_SORT_ATTRIBUTE = 'sortorder'
SHOW_ARCHIVES = True
LINKS = (
    ('blog tags', '/tags'),
    ('archive', '/archives'),
)

# Social widget
SOCIAL_WIDGET_NAME = 'Find me here'
SOCIAL = (
    ('twitter', 'http://twitter.com/greenkey'),
    ('linkedin', 'http://linkedin.com/in/lorenzomele'),
    ('github', 'http://github.com/greenkey'),
    ('devto', 'https://dev.to/greenkey'),
)

# other settings
DEFAULT_PAGINATION = 10
GOOGLE_ANALYTICS = 'UA-55895-1'
