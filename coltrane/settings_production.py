from settings import *

# Django settings for yoursite project in PRODUCTION mode.
TEMPLATE_DEBUG = DEBUG = False

# FIXME: put your contact details here for when 500s occur
ADMINS = (
    ('Your name here', 'you@yours.com'),
)
MANAGERS = ADMINS

# FIXME: enter your own production DB logins here
DATABASE_USER = 'mysite'
DATABASE_PASSWORD = 'myreallysecurepassword'

# FIXME: enter your own static content server details here
MEDIA_URL = 'http://mediasite.com'

ROOT_URLCONF = 'apps.urls_production'