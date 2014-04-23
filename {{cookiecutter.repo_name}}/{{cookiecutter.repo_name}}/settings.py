# Django settings for {{ cookiecutter.project_name }} project.
import os
from os import path

PROJECT_DIR = path.dirname(path.abspath(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS


# Brand configuration
BRAND_NAME = '{{ cookiecutter.project_name }}'

BRAND_ROOT = os.environ.get(
    'BRAND_ROOT',
    path.realpath(path.join(PROJECT_DIR, '..', 'brands', BRAND_NAME)))

BRAND = {
    'name': BRAND_NAME,
    # Prevents non-registered users to see content
    'public': True,
    # logo url if any
    'logo': None,
    # brand root contains templates and statics
    'root': BRAND_ROOT,
}

FEATURED_COLLECTION = 42
FEATURED_COLLECTIONS = [42, 44]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.dat',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': '{{ cookiecutter.project_name }}',
        'TIMEOUT': 60,
        'KEY_PREFIX': os.environ.get('MEMCACHED_KEY_PREFIX', '{{ cookiecutter.project_name }}'),
        'OPTIONS': {
            'MAX_ENTRIES': 10000,
            'CULL_FREQUENCY': 3,
        }
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Europe/Paris'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

LOCALE_PATHS = (
    path.realpath(path.join(PROJECT_DIR, '..', 'locale')),
)

LANGUAGES = (
    ('fr', 'French'),
    ('en', 'English'),
)

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
if path.isdir(path.expanduser('~/root/var')):
    MEDIA_ROOT = path.expanduser('~/root/var/media/')
else:
    MEDIA_ROOT = path.realpath(path.join(PROJECT_DIR, '..', 'media'))

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/medias/'

ADMIN_MEDIA_PREFIX = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = path.join(PROJECT_DIR, '..', 'static')

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'


DEVELOP_DIR = path.join(PROJECT_DIR, '..', 'src')
if not path.isdir(DEVELOP_DIR):
    DEVELOP_DIR = path.expanduser('~/root/var/share/')

# Additional locations of static files
STATICFILES_DIRS = (
    path.join(PROJECT_DIR, 'static'),
    path.join(BRAND_ROOT, 'static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'tw0v@dg(p%kn!l3wj(r8h450n)=a!qg5hpww98e4p%ooa*fj8^'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'accounts.middleware.Private',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.request",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "{{ cookiecutter.project_name }}.jstools.context_processors",
    'social.apps.django_app.context_processors.backends',
)

ROOT_URLCONF = '{{ cookiecutter.project_name }}.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = '{{ cookiecutter.project_name }}.wsgi.application'

TEMPLATE_DIRS = (
    path.realpath(path.join(PROJECT_DIR, '..', 'templates')),
    path.realpath(path.join(BRAND_ROOT, '..', 'templates')),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.comments',

    'south',
    'registration',
    'social.apps.django_app.default',
    'taggit',
    'autoslug',
    'bootstrap3',
)

LOGIN_URL          = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'
LOGIN_ERROR_URL    = '/accounts/login-error'

from django.template.defaultfilters import slugify

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
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


if path.isdir(path.expanduser('~/root/var')):
    CACHE_DIRECTORY = path.expanduser('~/root/var/cache/')
else:
    CACHE_DIRECTORY = path.join(MEDIA_ROOT, 'cache')
