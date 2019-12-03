# Standard library imports
import logging

# Related third party imports


# Local application/library specific imports
from log import LOG_SETTINGS
from django.urls import path

from . import views

logging.config.dictConfig(LOG_SETTINGS)

logger = logging.getLogger('__main__')

urlpatterns = [
    path('', views.index, name='index'),
]
