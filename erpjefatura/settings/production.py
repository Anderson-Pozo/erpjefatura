from .base import *

DEBUG = True
ALLOWED_HOSTS = ['erpjefatura.herokuapp.com']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

STATIC_URL = '/static/'
STATICFILES_DIRS = (BASE_DIR, 'static')
