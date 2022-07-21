# collection of commands
# not intended to be run as a script


# check tables postgresql
select * from information_schema.tables where table_name like 'api%'

# clear table 'x' postgresql
DELETE FROM x

# seed database
python3 src_db/seed.py

# run vue
nvm use 16.15.1
npm run serve

