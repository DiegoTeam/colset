import os
import time

from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')

app = Celery('colset')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


# TODO: Remove this task
@app.task(bind=True, name='sum-of-two-numbers')
def add(self, x, y):
    """
    This is a test task to interact with celery functionalities.

    Parameters
    ----------
    self
        Refer to the current task instance.
    x : int
        First number to add
    y : int
        Second number to add
    """
    total = 20
    progress = 0

    for index in range(1, total + 1):
        progress = ((index / total) * 100.0)
        self.update_state(
            state='PROGRESS',
            meta={'done': index, 'total': total, 'progress': progress, 'result': ''}
        )
        time.sleep(1)

    return {'done': index, 'total': total, 'progress': progress, 'result': f'{x + y}'}
