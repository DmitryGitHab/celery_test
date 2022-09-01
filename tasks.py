import time
from celery import Celery

celery_app = Celery(broker='redis://127.0.0.1:6379/1',
                    backend='redis://127.0.0.1:6379/2')


@celery_app.task
def hard_work_func(a,b):
    time.sleep(1)
    return a+b
