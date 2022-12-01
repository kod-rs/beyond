#!/bin/sh
sudo cp -R ../../src_django ./src_django/
sudo cp -R ../../schemas ./schemas/
sudo cp ../../manage.py ./manage.py
sudo cp ../../requirements.pip.txt ./requirements.pip.txt
sudo cp ../../.env ./.env
sudo docker build . -t backend