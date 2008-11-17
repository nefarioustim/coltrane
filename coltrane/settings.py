import sensitive # Assumed to be in the same directory.

# Django settings for cms project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = (
	('Tim Huegdon', 'tim@nefariousdesigns.co.uk'),
)

DATABASE_ENGINE = 'mysql'
DATABASE_NAME = sensitive.DATABASE_NAME
DATABASE_USER = sensitive.DATABASE_USER
DATABASE_PASSWORD = sensitive.DATABASE_PASSWORD
DATABASE_HOST = sensitive.DATABASE_HOST
DATABASE_PORT = sensitive.DATABASE_PORT

AKISMET_API_KEY = sensitive.AKISMET_API_KEY

DELICIOUS_USER = sensitive.DELICIOUS_USER
DELICIOUS_PASSWORD = sensitive.DELICIOUS_PASSWORD

EMAIL_USE_TLS = sensitive.EMAIL_USE_TLS
EMAIL_HOST = sensitive.EMAIL_HOST
EMAIL_HOST_USER = sensitive.EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = sensitive.EMAIL_HOST_PASSWORD
EMAIL_PORT = sensitive.EMAIL_PORT

# INTERNAL_IPS = (
# 	'127.0.0.1',
# )

# Local time zone for this installation. Choices can be found here:
# http://www.postgresql.org/docs/8.1/static/datetime-keywords.html#DATETIME-TIMEZONE-SET-TABLE
# although not all variations may be possible on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'GB'

# Language code for this installation. All choices can be found here:
# http://www.w3.org/TR/REC-html40/struct/dirlang.html#langcodes
# http://blogs.law.harvard.edu/tech/stories/storyReader$15
LANGUAGE_CODE = 'en-gb'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT.
# Example: "http://media.lawrence.com"
MEDIA_URL = ''

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '&v_+z9$b5c&md&*i!8i46lcfy7nwspi7@_f2x(r9@cdg*jd12j'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.doc.XViewMiddleware',
	# 'debug_toolbar.middleware.DebugToolbarMiddleware',
)

ROOT_URLCONF = 'cms.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
	'/Users/huegdon/projects/django/coltrane/templates',
)

INSTALLED_APPS = (
	# 'debug_toolbar',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
	'django.contrib.admin',
	'django.contrib.flatpages',
	'django.contrib.comments',
	'django.contrib.markup',
	'coltrane',
	'tagging',
)