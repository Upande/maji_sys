from base import *

import dj_database_url

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    #'default': dj_database_url.config(default='postgres://postgres:postgres@192.168.3.4:5432/wrma_test_db')
    'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'OPTIONS': {
                'options': '-c search_path=fews,public'
            },
            'NAME': 'wrma_final_db',
            'USER': 'postgres',
            'PASSWORD': 'postgres',
            'HOST': '127.0.0.1',
            'PORT': '5432',
    }
}

THIRD_PARTY_APPS = []

LOCAL_APPS = [
    'maji_sys',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

LOGIN_REDIRECT_URL = 'data_form'

USE_DJANGO_JQUERY = False

