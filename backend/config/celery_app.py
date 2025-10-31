from .celery import celery_app as app

# Expose as `celery_app` too, if referenced directly
celery_app = app