#! /bin/bash
uv run --group prod manage.py makemigrations
uv run --group prod manage.py migrate
uv run --group prod gunicorn quotevote.wsgi:application 0.0.0.0:10000
