"""
Django settings for oarepo project.

Generated by 'django-admin startproject' using Django 1.9.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
from django.utils.translation import ugettext_lazy as _

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ct79($rugpit$d+d_t@b$m2t2(4bq)9bk^8^qv!ug%px8-^uxe'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'fedoralink',
    'fedoralink_ui',
    'baseOArepo',
    'dcterms',
    'bootstrap_pagination',
    'bootstrap3',
    # 'changeRDFtype',
    # 'createTypes',
    'romiste',
    # 'fedoralink.common_namespaces.web_acl',
    # 'state_engine',
    # 'types_engine',
    'administration',
    'data_types',
    #'urlbreadcrumbs',
    'django.contrib.admin',
    'autobreadcrumbs'
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

MIDDLEWARE_CLASSES += [
'fedoralink.middleware.FedoraUserDelegationMiddleware'
]

CONTEXT_PROCESSORS = [
'django.template.context_processors.debug',
'django.template.context_processors.request',
'django.contrib.auth.context_processors.auth',
'django.contrib.messages.context_processors.messages',
'django.template.context_processors.i18n',
'django.template.context_processors.media',
'django.template.context_processors.static',
'django.template.context_processors.tz',
]


CONTEXT_PROCESSORS += [
'oarepo.context_processors.AutoBreadcrumbsContext'
]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(os.path.dirname(__file__), 'debug.log'),
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
#         'LOCATION': 'unique-snowflake',
#     }
# }

LANGUAGES = (
    ('cs', _('Čeština')),
    ('en', _('English')),
)

ROOT_URLCONF = 'oarepo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': CONTEXT_PROCESSORS,
        },
    },
]

WSGI_APPLICATION = 'oarepo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

import socket
DATABASES['repository'] = {
    'ENGINE'          : 'fedoralink.engine',
    'SEARCH_ENGINE'   : 'fedoralink.indexer.elastic.ElasticIndexer',
    #'REPO_URL'        :  'http://127.0.0.1:8090/fcrepo-webapp-plus-webac-audit-4.7.1/rest/',
    'REPO_URL'        : 'http://127.0.0.1:8080/fcrepo/rest',
    'SEARCH_URL'      : 'http://127.0.0.1:9200/oarepo',
    'USE_INTERNAL_INDEXER' : True,
    'USERNAME'        : 'oarepo',#'admin',#'cis_repo',#
    'PASSWORD'        : '9R4eKekrWjzEiFwtHsyRdPFnywarwqdtMUeR'#'admin'#'5SKJ4KW6NyxdSNwtxC8uoE9VAPVKJ37qLQ3DTJR6Wvz6rHSh'#
}

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    # {
    #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    # },
]


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'

USE_BREADCRUMBS=True

LOGOUT_REDIRECT_URL = '/'
LOGIN_REDIRECT_URL = '/'

USERS_TOMCAT_PASSWORD = 'user1pw'