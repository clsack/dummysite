from __future__ import absolute_import, unicode_literals
import os

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dummyapp.settings.environment')
from django.conf import settings
from celery import Celery


app = Celery('dummyapp', include=['dummyapp.tasks'])

app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
from django.apps import apps
app.autodiscover_tasks(lambda: [n.name for n in apps.get_app_configs()])


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
