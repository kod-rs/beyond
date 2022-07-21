# keycloak-18.0.1

# start server
./bin/kc.sh start-dev

# export configuration
./bin/kc.sh export --dir export_dir_name

# runs on
http://localhost:8080/

# todo for prod
https://www.keycloak.org/docs/latest/server_installation/
ssl

curl -L -X GET 'http://localhost:8080/realms/beyond/protocol/openid-connect/certs'