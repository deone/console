from settings import *

DEBUG = False

STATIC_ROOT = '/home/deone/webapps/console_static'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'sql_mode': 'traditional',
        },
        'NAME': 'console_prod',
        'USER': 'console_admin',
        'PASSWORD': 'c0ns0l3',
        'HOST': '127.0.0.1',
        'PORT': '3306'
    }
}