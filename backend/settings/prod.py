""" Production Settings """

import os
import dj_database_url
# from .dev import *
from .dev import *  # NOQA

############
# DATABASE #
############
DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv('DATABASE_URL')
    )
}

############
# SECURITY #
############

DEBUG = bool(os.getenv('DJANGO_DEBUG', ''))

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', SECRET_KEY)

# Set to your Domain here (eg. 'django-vue-template-demo.herokuapp.com')
ALLOWED_HOSTS = ['*']

from .dev import *  # NOQA
DEBUG = False
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
MIDDLEWARE = [*MIDDLEWARE,
              'django.middleware.security.SecurityMiddleware']
SECURE_HSTS_SECONDS = 1
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_SSL_REDIRECT = True
SECURE_HSTS_PRELOAD = True