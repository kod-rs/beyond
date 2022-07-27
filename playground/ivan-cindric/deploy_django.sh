
#python3 ../../manage.py migrate
#python3 ../../manage.py makemigrations
export DJANGO_SETTINGS_MODULE=backend.settings.prod
python3 ../../manage.py check --deploy
python3 ../../manage.py runserver