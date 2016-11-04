from .base import *


# Removing security enforcement in development mode

DEBUG = True

SECRET_KEY = env('DJANGO_SECRET_KEY', '1234567890')

INTERNAL_IPS = ['127.0.0.1']

ALLOWED_HOSTS = []


# Enabling console loggers

LOGGING['loggers'] = {
    'django': {
        'handlers': ['console'],
        'level': env('DJANGO_LOG_LEVEL', 'INFO'),
    },
    'toy': {
        'handlers': ['console'],
        'level': env('TOY_LOG_LEVEL', 'DEBUG'),
    },
}
