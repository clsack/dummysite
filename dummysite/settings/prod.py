import os
from .base import BASE_DIR

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(axxx!ri=8)fsko-zl5$*uz(@)&5hgptc0l-hx-6t*=+d2d=tv'

DEBUG = False

ALLOWED_HOSTS = ['*']

STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
