from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab
# from datetime import timedelta


# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scheduling_sms_on_phone_django.settings')

app = Celery('scheduling_sms_on_phone_django')
app.conf.enable_utc=False
app.conf.update(timezone='Asia/Kolkata')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object(settings, namespace='CELERY')


# Load task modules from all registered Django apps.
# Celery Beat tasks registration
app.conf.beat_schedule = {

    'Send_sms_to_Client': {
        'task': 'send_sms.task.send_sms_phone',
        # 'schedule': timedelta(seconds=300),
        'schedule': crontab(minute='*/1'),
        'args': ('+917982102159', 'Hello, this is a scheduled message!')
    },

}

# 'schedule': 30.0, #every 30 seconds it will be called
# #'args': (2,) you can pass arguments also if rquired
# }
# }

app.autodiscover_tasks()
@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')