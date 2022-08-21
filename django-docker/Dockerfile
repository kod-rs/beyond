# syntax=docker/dockerfile:1
FROM ubuntu:22.04

ENV DEBIAN_FRONTEND noninteractive
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR .

RUN apt-get update
RUN apt-get install -y python3-pip
RUN apt-get install -y libpq-dev
RUN apt-get install -y mkcert
RUN apt-get install -y libnss3-tools
RUN apt-get install -y python3.10-dev

ADD backend backend
COPY wait-for-it.sh wait-for-it.sh
COPY env env
COPY manage.py manage.py
COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock
COPY requirements.pip.txt requirements.pip.txt
COPY run_django.sh run_django.sh

EXPOSE 8000

RUN pip install -r requirements.pip.txt
CMD ["./run_django.sh"]
