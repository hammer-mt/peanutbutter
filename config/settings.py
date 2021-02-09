import os
from distutils.util import strtobool
from datetime import timedelta


SERVER_NAME = os.getenv('SERVER_NAME',
                        'localhost:{0}'.format(os.getenv('DOCKER_WEB_PORT',
                                                         '8000')))

# Celery.
CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL', 'redis://redis:6379/0')
CELERY_RESULT_BACKEND = CELERY_BROKER_URL
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_REDIS_MAX_CONNECTIONS = 5
CELERYBEAT_SCHEDULE = {}

CELERYBEAT_SCHEDULE.update({
    'run_every_5s': {
        'task': 'peanutbutter.contact.tasks.deliver_contact_email_cron',
        'schedule': timedelta(seconds=5),
        'args': ({"email": "mike@example.com", "message": "cron job is working"},)
    }
})