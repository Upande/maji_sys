from base import *

import dj_database_url

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.config(default='postgres://postgres:postgres@192.168.1.27:5432/wrma_test')
}

THIRD_PARTY_APPS = []

LOCAL_APPS = [
    'maji_sys',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

LOGIN_REDIRECT_URL = 'index'