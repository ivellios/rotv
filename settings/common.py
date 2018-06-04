# -*- coding: utf-8 -*-
import os, sys
import datetime

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# sys.path.append(os.path.join(BASE_DIR, 'apps'))

INSTALLED_APPS = (
    # admin 3rd party apps
    'tinymce',
    'grappelli.dashboard',
    'grappelli',
    'adminactions',
    'filebrowser',
    # django built-in apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    # local apps
    'rotv_apps.program',
    'rotv_apps.blog',
    'rotv_apps.heros',
    'rotv_apps.navigations',
    'rotv_apps.partners',
    'rotv_apps.shortener',

    'django_extensions',
    'easy_thumbnails',
    'tagging',
    'material',
)

GRAPPELLI_INDEX_DASHBOARD = 'ro.dashboard.CustomIndexDashboard'
SITE_ID = 1

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'staticflatpages.middleware.StaticFlatpageFallbackMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
]

ROOT_URLCONF = 'ro.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR + '/templates/', ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'ro/static'),
]

# WSGI_APPLICATION = 'ro.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'pl'

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Warsaw'
USE_TZ = True

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True
USE_L10N = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/
STATIC_ROOT = BASE_DIR + '/public/static/'
STATIC_URL = '/static/'
MEDIA_ROOT = BASE_DIR + '/public/media/'
MEDIA_URL = '/media/'

FILEBROWSER_EXTENSIONS = {
    'Folder': [''],
    'Image': ['.jpg', '.jpeg', '.gif', '.png', '.tif', '.tiff'],
    'Zip': ['.zip', '.rar'],
    'Video': ['.mov', '.wmv', '.mpeg', '.mpg', '.avi', '.rm'],
    'Document': ['.pdf', '.doc', '.rtf', '.txt', '.xls', '.csv'],
    'Sound': ['.mp3', '.mp4', '.wav', '.aiff', '.midi'],
    'Code': ['.html', '.py', '.js', '.css']
}

ADMIN_MEDIA_PREFIX = '/static/admin/'

SOUTH_MIGRATION_MODULES = {
    'taggit': 'taggit.south_migrations',
}

NEWSLETTER_DEFAULT_HEADER_SENDER = 'Raport Obieżyświata <no-reply@raportobiezyswiata.tv>'
NEWSLETTER_RICHTEXT_WIDGET = 'tinymce.widgets.TinyMCE'

ALLOWED_HOSTS = []

LONG_ENTRY_LENGTH = 4000

THUMBNAIL_NAMER = 'easy_thumbnails.namers.source_hashed'

TINYMCE_DEFAULT_CONFIG = {
    'selector': 'textarea',
    'theme': 'modern',
    'plugins': 'link image preview codesample contextmenu table code lists fullscreen',
    'toolbar1': 'bold italic underline | alignleft aligncenter alignright alignjustify '
               '| bullist numlist | outdent indent | table | link image | codesample | preview code | fullscreen',
    'contextmenu': 'formats | link image',
    'menubar': False,
    'inline': False,
    'statusbar': True,
    'height': 360,
    'image_advtab': True,
    'invalid_elements': 'p[dir],span',
    'invalid_styles': {'p': 'font-weight,font-style,text-decoration,line-height,margin-top,margin-bottom,'
                            'color,background,background-color,font-size,font-family,vertical-align,white-space,'
                            'font-variant,list-style-type,margin,padding'},
    'image_class_list': [
        {'title': 'No float', 'value': ''},
        {'title': 'Float right', 'value': 'img_right'},
        {'title': 'Float left', 'value': 'img_left'},
        {'title': 'Display block', 'value': 'img_block'}
    ],
    'content_css': STATIC_URL + 'css/admin.css',
}

TINYMCE_CSS_URL = STATIC_URL + 'css/admin.css'

SHORTENER_BASE_URL = 'https://rotv.yt'
