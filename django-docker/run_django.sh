#!/bin/sh
./wait-for-it.sh localhost:5432
python3 manage.py migrate
python3 manage.py makemigrations
python3 manage.py runserver 
