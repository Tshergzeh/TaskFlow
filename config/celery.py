import os
from pathlib import Path

from celery import Celery
import environ

# Take environment variables from .env file
BASE_DIR = Path(__file__).resolve().parent.parent
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

env = environ.Env(
    DJANGO_SETTINGS_MODULE='config.settings'
)

app = Celery('config', broker=env('REDIS_LOCATION'))

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
    