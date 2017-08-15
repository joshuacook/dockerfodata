#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Josh Cook'
SITENAME = 'Docker For Data Science'
#SITEURL = 'http://www.dockerfordatascience.com'

PATH = 'content'

PLUGINS = ["render_math"]

TIMEZONE = 'America/Dawson'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Docker fo Data Science on Amazon', 'hhttps://www.amazon.com/Docker-Data-Science-Extensible-Infrastructure/dp/1484230116/ref=sr_1_1?ie=UTF8&qid=1501386076&sr=8-1&keywords=docker+for+data+science'),
         ('Python.org', 'http://python.org/'),
         ('Docker', 'https://www.docker.com/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 3

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
