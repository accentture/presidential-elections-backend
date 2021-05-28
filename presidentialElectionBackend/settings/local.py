#importing all code from base.py
from .base import *
import os

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

CORS_ORIGIN_WHITELIST = (
    'http://localhost:4200',
    'https://eleccionesperu2021.netlify.app'
)
STATIC_URL = '/static/'

# ================== configurations to upload image
MEDIA_URL = '/media/' # indiccating what is name where will be saved multimedia files
MEDIA_ROOT = os.path.join(BASE_DIR, 'media') 



