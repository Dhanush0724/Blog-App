web: gunicorn BLOGGING.wsgi --log-file -
worker: celery -A BLOGGING worker --loglevel=info
