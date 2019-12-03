import os
from .base import BASE_DIR

DEBUG = True

ALLOWED_HOSTS = []

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static/"),
]
