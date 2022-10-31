from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')

app.config_from_object('django.config:settings', namespace='CELERY')

app.autodiscover_tasks()
app.conf.schedule_beat = {
    'crawl-every-day': {
        'task': 'api_news.tasks.crawl_newsfeed',
        'schedule': '* * * * *'
    }
}


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
