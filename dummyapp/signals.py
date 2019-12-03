# Standard library imports
import logging

# Related third party imports


# Local application/library specific imports
from log import LOG_SETTINGS

logging.config.dictConfig(LOG_SETTINGS)
logger = logging.getLogger('dummyapp')
