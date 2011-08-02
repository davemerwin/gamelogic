import os
PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))
ACCOUNT_ACTIVATION_DAYS = 4
ADMINS = (('Dave Merwin', 'dave@davemerwin.com'),)
ADMIN_MEDIA_PREFIX = 'http://s3.amazonaws.com/djangoadmin1.3/media/'
DEBUG = False
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.flatpages',
    'django.contrib.markup',
    'django.contrib.comments',
    'story',
    'south',
)
LANGUAGE_CODE = 'en-us'
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
MANAGERS = ADMINS
MEDIA_ROOT = ''
MEDIA_URL = ''
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)
ROOT_URLCONF = 'gamelogic.urls'
SECRET_KEY = 'hr5tyz^+++pu-#6i3ngv&e6x8u5%8-5ro0hsl$8gly&jd(=hv9'
SITE_ID = 1
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.core.context_processors.static',
)
TEMPLATE_DEBUG = DEBUG
TEMPLATE_DIRS = (os.path.join(PROJECT_PATH, os.pardir, 'templates'))
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)
TIME_ZONE = 'PST8PDT'
USE_I18N = True
USE_L10N = True