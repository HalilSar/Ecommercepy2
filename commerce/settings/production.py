import os
from .base import *
with open(os.path.join(BASE_DIR,'secret_key.txt')) as f:
        SECRET_KEY = f.read().strip()
DEBUG = False
ALLOWED_HOSTS = ['halil37.pythonanywhere.com']
STATIC_ROOT = os.path.join(BASE_DIR,"static")
