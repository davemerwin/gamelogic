from base import *
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'merwin_gamelogic',                      # Or path to database file if using sqlite3.
        'USER': 'merwin_gamelogic',                      # Not used with sqlite3.
        'PASSWORD': '6d7d99eb',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}
DEBUG = False
MEDIA_ROOT = os.path.join(PROJECT_PATH, os.pardir, '..', '..', '..', 'gamelogic_media', 'dynamic')
MEDIA_URL = '/media/dynamic/'
STATIC_ROOT = ''
STATIC_URL = '/media/static/'
STATICFILES_DIRS = (os.path.join(PROJECT_PATH, os.pardir, '..', '..', '..', 'gamelogic_media', 'static'),)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)