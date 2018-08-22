"""
Django settings for hrdc project.

Generated by 'django-admin startproject' using Django 1.11.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
from django.contrib import messages

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ''

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'config',
    'emailtracker',
    'basetemplates',
    'chat',
    'hrdc',
    'django.contrib.humanize',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'dramaorg',
    'casting',
    'bootstrapform',
    'anymail',
    'channels',
]

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "asgiref.inmemory.ChannelLayer",
        "ROUTING": "hrdc.routing.channel_routing",
    },
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'hrdc.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'basetemplates.context_processor',
            ],
        },
    },
]

WSGI_APPLICATION = 'hrdc.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

CSRF_USE_SESSIONS = True

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'US/Eastern'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

MESSAGE_TAGS = {
    messages.DEBUG: 'debug',
    messages.INFO: 'info',
    messages.SUCCESS: 'success',
    messages.WARNING: 'warning',
    messages.ERROR: 'danger',
}

AUTH_USER_MODEL = "dramaorg.User"

SHOW_MODEL = "dramaorg.Show"
SPACE_MODEL = "dramaorg.Space"
BUILDING_MODEL = "dramaorg.Building"

ANYMAIL = {
    "MAILGUN_API_KEY": "",
    "MAILGUN_SENDER_DOMAIN": ""
}
EMAIL_BACKEND = "anymail.backends.mailgun.EmailBackend"

DEFAULT_FROM_EMAIL = "HRDC Apps <user@domain.com>"

CONFIGURATION_APP_TITLE = "Global Settings"

ADMIN_SITE_TITLE = "HRDC Apps"

ADMIN_GROUP_NAME = "HRDC Board"

LOGIN_URL = "dramaorg:login"
LOGOUT_URL = "dramaorg:logout"
LOGIN_REDIRECT_URL = "dramaorg:index"
LOGOUT_REDIRECT_URL = LOGIN_URL

LOGO_PATH = os.path.join(BASE_DIR, "hrdc/static/logo.png")

BT_SITE_TITLE = "HRDC Apps"
BT_FAVICON_URL = STATIC_URL + "icon.png"
BT_BOOTSTRAP_VERSION = "4.0.0-beta.3"
BT_BOOTSTRAP_CSS_INTEGRITY = "sha384-Zug+QiDoJOrZ5t4lssLdxGhVrurbmBWopoEl+M6BdEfwnCJZtKxi1KgxUyJq13dy"
BT_BOOTSTRAP_JS_INTEGRITY = "sha384-a5N7Y/aK3qNeh15eJKGWxsqtnX/wWdSZSKp+81YjTmS15nvnvxKHuzaWwXHDli+4"
BT_POPPER_VERSION = "1.12.9"
BT_POPPER_INTEGRITY = "sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q"

FOOTER_OWNER = "Harvard-Radcliffe Dramatic Club"
FOOTER_SITE = "http://hrdctheater.com"
BT_HEADER_IMAGE = "logo.png"
BT_HEADER_URL = "dramaorg:index"

BT_JS_FILES = ["profilefields.js"]

GROUP_LOCATION = "Harvard"
SITE_URL = "http://localhost:8000"

CASTING_IS_COMMON = True

ACTIVE_SEASON_KEY = "season"
ACTIVE_YEAR_KEY = "year"

CELERY_BEAT_SCHEDULE = {
    'update-casting-releases': {
        'task': 'casting.tasks.update_releases',
        'schedule': 10.0,
        'relative': True,
    },
    'send-missed-emails': {
        'task': 'emailtracker.tasks.send_missing',
        'schedule': 60.0 * 10.0,
        'relative': False,
    },
}

QUEUED_EMAIL_TEMP = None
QUEUED_EMAIL_DEBUG = False

CHAT_LOADING_LIMIT = 80
