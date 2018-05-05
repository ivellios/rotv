# -*- coding: utf-8 -*-
from os import environ

from settings.common import *

read_env = lambda e, d=None: environ[e] if environ.has_key(e) else d

DEBUG = os.environ.get('ROTV_STAGING_DJANGO_DEBUG')
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': read_env('ROTV_STAGING_DB_NAME'),                      # Or path to database file if using sqlite3.
        'USER': read_env('ROTV_STAGING_DB_USER'),                      # Not used with sqlite3.
        'PASSWORD': read_env('ROTV_STAGING_DB_PASS'),                  # Not used with sqlite3.
        'HOST': read_env('ROTV_STAGING_DB_HOST'),                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

ALLOWED_HOSTS += [
    'staging.raportobiezyswiata.tv',
]

SECRET_KEY = read_env('ROTV_STAGING_SECRET')


ALLOWED_HOSTS += [
    'staging.raportobiezyswiata.tv',
    'www.staging.raportobiezyswiata.pl',
]

EMAIL_HOST = read_env('ROTV_STAGING_EMAIL_HOST')
EMAIL_PORT = read_env('ROTV_STAGING_EMAIL_PORT')
EMAIL_HOST_USER = read_env('ROTV_STAGING_EMAIL_USERNAME')
EMAIL_HOST_PASSWORD = read_env('ROTV_STAGING_EMAIL_PASSWORD')

ROOT_URL = 'http://staging.raportobiezyswiata.tv'

PATRONAGE_MANAGERS = ['just_checking@mailtrap.io']
