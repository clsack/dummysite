# Standard library imports


# Related third party imports
from celery.task.schedules import crontab
from celery.decorators import periodic_task

# Local application/library specific imports
from django.conf import settings

#logger = get_task_logger(__name__)


@periodic_task(run_every=(crontab(minute='*/5')), name="task_get_combinations")
def task_get_combinations():
    pass
