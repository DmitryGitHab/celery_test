docker-compose up

run from WSL (linux):

    pip install celery,
    pip install redis,
    celery -A tasks.celery_app worker -c4    
    (c4 - явно указывается количество потоков)

run main