from .base import * 
SECRET_KEY = 'django-insecure-i)6%h6ax_-uzppy@g1=%#@an0zholm@5#adu1a6ao8u)o=ht+g'
DEBUG = True
ALLOWED_HOSTS = []
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
STATIC_ROOT = os.path.join(BASE_DIR, "static")