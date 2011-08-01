from base import *
import os
PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'gamelogic.db',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}
DEBUG = True
#DEBUG_TOOLBAR_CONFIG = {
#    'INTERCEPT_REDIRECTS' : False,
#}
#INTERNAL_IPS = ('127.0.0.1',)
#INSTALLED_APPS += (
#    'debug_toolbar',
#)
#MIDDLEWARE_CLASSES += (
#    'debug_toolbar.middleware.DebugToolbarMiddleware',
#)
MEDIA_ROOT = os.path.join(PROJECT_PATH, os.pardir, '..', 'media', 'dynamic')
MEDIA_URL = '/media/dynamic/'
STATIC_ROOT = ''
STATIC_URL = '/media/static/'
STATICFILES_DIRS = (os.path.join(PROJECT_PATH, os.pardir, '..', 'media', 'static'),)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
TEMPLATE_DEBUG = DEBUG