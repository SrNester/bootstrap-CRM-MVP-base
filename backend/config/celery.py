import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

celery_app = Celery('crm_backend')
celery_app.conf.broker_url = os.environ.get('REDIS_URL', 'redis://redis:6379/0')
celery_app.conf.result_backend = os.environ.get('REDIS_URL', 'redis://redis:6379/0')

celery_app.autodiscover_tasks()