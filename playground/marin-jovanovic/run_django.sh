# collection of commands
# not intended to be run as a script

# activate venv
source venv/bin/activate

# to add new model
python3 manage.py makemigrations
python3 manage.py migrate

# run backend
python3 manage.py runserver

# check tables postgresql
select * from information_schema.tables where table_name like 'api%'

# seed database
python3 src_db/seed.py