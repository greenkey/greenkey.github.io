#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'greenkey'
SITENAME = 'loman.it'
SITESUBTITLE = 'home of Lorenzo Mele'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = 'en'

GITHUB_URL = 'https://github.com/greenkey'
TWITTER_USERNAME = 'greenkey'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
SOCIAL_WIDGET_NAME = 'Social'
SOCIAL = (('Twitter', 'http://twitter.com/' + TWITTER_USERNAME),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Specify name of a built-in theme
#THEME = "simple"

MENUITEMS = [
	('Me', 'me')
]