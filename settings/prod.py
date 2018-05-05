# -*- coding: utf-8 -*-
from os import environ

from settings.common import *

read_env = lambda e, d=None: environ[e] if environ.has_key(e) else d

DEBUG = False
TEMPLATE_DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': read_env('ROTV_PROD_DB_NAME'),                      # Or path to database file if using sqlite3.
        'USER': read_env('ROTV_PROD_DB_USER'),                      # Not used with sqlite3.
        'PASSWORD': read_env('ROTV_PROD_DB_PASS'),                  # Not used with sqlite3.
        'HOST': read_env('ROTV_PROD_DB_HOST'),                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

SECRET_KEY = read_env('ROTV_PROD_SECRET')


ALLOWED_HOSTS += [
    'raportobiezyswiata.tv',
    'raportobiezyswiata.pl',
    'www.raportobiezyswiata.tv',
    'www.raportobiezyswiata.pl',
    'rotv.yt'
]

# EMAIL SETTINGS
EMAIL_HOST = read_env('ROTV_PROD_EMAIL_HOST')
EMAIL_PORT = read_env('ROTV_PROD_EMAIL_PORT')
EMAIL_HOST_USER = read_env('ROTV_PROD_EMAIL_USERNAME')
EMAIL_HOST_PASSWORD = read_env('ROTV_PROD_EMAIL_PASSWORD')

PATRONAGE_MANAGERS = ['patronat@raportobiezyswiata.tv']

ROOT_URL = 'http://raportobiezyswiata.tv'
