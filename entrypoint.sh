#!/bin/sh
python3 manage.py makemigrations --noinput
python3 manage.py migrate
DJANGO_SUPERUSER_PASSWORD=test python3 manage.py createsuperuser --username test --email test@gamil.com --noinput
python3 manage.py runserver 0.0.0.0:8000