from src_django.settings.dev import *  # NOQA

DEBUG = False

DEVELOPMENT_MODE = False

# SECURITY WARNING: Set this to True to avoid transmitting the
# session cookie over HTTP accidentally.

SESSION_COOKIE_SECURE = True

# SECURITY WARNING: Set this to True to avoid transmitting the CSRF cookie over
# HTTP accidentally.

CSRF_COOKIE_SECURE = True

# SECURITY WARNING: This setting is required to protect your site against some
# CSRF attacks. If you use a wildcard, you must perform your own validation
# of the Host HTTP header, or otherwise ensure that you aren’t vulnerable to
# this category of attacks (e.g ['www.mysite.hr']). This value defaults to
# localhost.

ALLOWED_HOSTS = ['*']

# SECURITY WARNING: If True, the SecurityMiddleware redirects all non-HTTPS
# requests to HTTPS.

SECURE_SSL_REDIRECT = False

# SECURITY WARNING: For sites that should only be accessed over HTTPS, you
# can instruct modern browsers to refuse to connect to your domain name via
# an insecure connection (for a given period of time). When enabling HSTS,
# it’s a good idea to first use a small value for testing, for example,
# SECURE_HSTS_SECONDS = 3600 for one hour. Each time a web browser sees the
# HSTS header from your site, it will refuse to communicate non-securely
# (using HTTP) with your domain for the given period of time.

SECURE_HSTS_SECONDS = 0

with open(HOME_LOCATION + '/secret_key.txt') as f:
    SECRET_KEY = f.read().strip()
