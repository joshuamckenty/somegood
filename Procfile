# web: alembic upgrade head && uwsgi --py-autoreload --ini deploy.ini
#web: uwsgi --py-autoreload --ini deploy.ini
web: gunicorn somegood:app
