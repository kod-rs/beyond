# syntax=docker/dockerfile:1
FROM ubuntu:22.04

RUN DEBIAN_FRONTEND=noninteractive DEBCONF_NOWARNINGS=yes apt-get update -y
RUN DEBIAN_FRONTEND=noninteractive DEBCONF_NOWARNINGS=yes apt-get install -y python3-pip
RUN DEBIAN_FRONTEND=noninteractive DEBCONF_NOWARNINGS=yes apt-get install -y libpq-dev
RUN DEBIAN_FRONTEND=noninteractive DEBCONF_NOWARNINGS=yes apt-get install -y libnss3-tools
RUN DEBIAN_FRONTEND=noninteractive DEBCONF_NOWARNINGS=yes apt-get install -y python3.10-dev
RUN DEBIAN_FRONTEND=noninteractive DEBCONF_NOWARNINGS=yes apt-get install -y python3.10-venv

COPY requirements.pip.txt requirements.pip.txt
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN pip install -r requirements.pip.txt

ADD src_django src_django
ADD schemas schemas
COPY .env .env
COPY manage.py manage.py
COPY run_backend.sh run_backend.sh
COPY add_env.py add_env.py
ADD beyond_keys beyond_keys
ADD flexopt_keys flexopt_keys

RUN python3 add_env.py

EXPOSE 8000

CMD ["./run_backend.sh"]
