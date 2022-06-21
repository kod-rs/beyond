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

# clear table 'x' postgresql
DELETE FROM x

# seed database
python3 src_db/seed.py

# run vue
nvm use 16.15.1
npm run serve

# keycloak-18.0.1
# serves on localhost:8080
./bin/kc.sh start-dev

#
http://localhost:8080/realms/beyond_realm/