import os

ADMINS = (('Jon Parise', 'jon@indelible.org'),)
MANAGERS = ADMINS
TIME_ZONE = 'PST5PDT'
LANGUAGE_CODE = 'en-us'
USE_I18N = False

MEDIA_ROOT = ''
MEDIA_URL = ''
TEMPLATE_DIRS = [os.path.join(os.path.dirname(__file__), "templates")]

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.markup',
    'django.contrib.sessions',
    'django.contrib.sitemaps',
    'django.contrib.sites',
    'django.contrib.webdesign',
    'ink',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

SITE_ID = 1
ROOT_URLCONF = 'indelible.urls'

CACHE_BACKEND = 'db://indelible_cache'
CACHE_MIDDLEWARE_SECONDS = 60 * 60 * 1 # 1 hour
CACHE_MIDDLEWARE_KEY_PREFIX = 'indelible'
CACHE_MIDDLEWARE_GZIP = True
CACHE_MIDDLEWARE_ANONYMOUS_ONLY = True

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# Ink
INK_FLAT_URLS = True
INK_DOCUTILS_SETTINGS = {'strip_comments': True,
                         'cloak_email_addresses': True,
                         'initial_header_level': 2}

# Import local settings
from settings_local import *
