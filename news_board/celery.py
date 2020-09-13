import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'news_board.settings')

app = Celery('news_board')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'reset-votes-every-day': {
        'task': 'main.tasks.reset_upvotes',
        'schedule': crontab(hour='*/24')
    },
}
