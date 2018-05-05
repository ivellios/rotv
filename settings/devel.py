from common import *
import os

SECRET_KEY = 'Keep it secret! Keep it safe!'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'ro.db',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

ALLOWED_HOSTS += [
    'localhost',
    'lvh.me',
]

DEBUG = True
TEMPLATE_DEBUG = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

ROOT_URL = 'http://localhost:8000'

PATRONAGE_MANAGERS = ['no-mail@no-mail.com']

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

EMAIL_HOST_USER = 'no-reply@domain.com'

try:
    from .settings_local import *
except ImportError:
    pass
