import os
from .base import *
with open(os.path.join(BASE_DIR,'secret_key.txt')) as f:
        SECRET_KEY = f.read().strip()
DEBUG = False
ALLOWED_HOSTS = ['halil37.pythonanywhere.com']
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'Halil37$default',
#         'USER': 'Halil37',
#         'PASSWORD': 'covboybebop123',
#         'HOST':'Halil37.mysql.pythonanywhere-services.com',
#     }
#}
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': 'commerce/settings/my.cnf',
        },
    }
}
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
STATIC_ROOT = os.path.join(BASE_DIR,"staticfiles")
