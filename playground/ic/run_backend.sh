#!/bin/sh
(cd ../../ && python manage.py migrate --run-syncdb)
(cd ../../ && python manage.py makemigrations)
(cd ../../ && python manage.py runserver)
