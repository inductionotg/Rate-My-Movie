from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MyMovie.settings')

app = Celery('MyMovie')
app.config_from_object('django.conf:settings')
app.conf.beat_schedule = {
    'add-every-30-seconds': {
        'task': 'TestApp.tasks.send_mail_task',
        'schedule':crontab(),
        #'args': ('pk',)
    }

}

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
@app.task(bind=True)
def debug_task(self):
    print('Request:{0!r}'.format(self.request))