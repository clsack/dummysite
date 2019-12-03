# Standard library imports
import logging

# Related third party imports


# Local application/library specific imports
from log import LOG_SETTINGS
from django import forms

logging.config.dictConfig(LOG_SETTINGS)

logger = logging.getLogger('__main__')
