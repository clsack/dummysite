# Standard library imports
import logging

# Related third party imports


# Local application/library specific imports
from log import LOG_SETTINGS
from django.apps import AppConfig

logging.config.dictConfig(LOG_SETTINGS)

logger = logging.getLogger('__main__')


class DummyappConfig(AppConfig):
    name = 'dummyapp'

    def ready(self):
        import dummyapp.signals
