"""
Django settings for socialnet project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')kj$s)hvxm1e*+*%y999lscot77=jpgmr_gh_qo3zbx7d-+tv+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []
DOMAIN_NAME = 'localhost:8000'

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'south',
    'account',
    'common',
    'socialapp',
    'registration',
    'djrill',
    'profiles',
    'django.contrib.formtools',
)

INSTALLED_APPS += (
    'debug_toolbar',
)
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',)

ROOT_URLCONF = 'socialnet.urls'

WSGI_APPLICATION = 'socialnet.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'socialnet',
        'USER': 'socialnet',
        'PASSWORD': 'socialnet'
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

STATIC_URL = '/static/'
AUTH_USER_MODEL = 'account.User'

TEMPLATE_DIRS = (
    '{0}/templates'.format(BASE_DIR),
)


# https://docs.djangoproject.com/en/1.6/ref/settings/
ACCOUNT_ACTIVATION_DAYS = 7  # One-week activation window; you may, of course, use a different value.

#https://docs.djangoproject.com/en/1.6/ref/settings/#default-from-email
DEFAULT_FROM_EMAIL = 'robot.socialnet@example.com'

#https://github.com/brack3t/Djrill
MANDRILL_API_KEY = "9lY6G-jlFEtJgEKXH0H0wg"
EMAIL_BACKEND = "djrill.mail.backends.djrill.DjrillBackend"

# https://docs.djangoproject.com/en/1.7/ref/settings/#login-url
LOGIN_URL = '/account/login/'

# https://docs.djangoproject.com/en/1.7/ref/settings/#login-redirect-url
LOGIN_REDIRECT_URL = '/'

