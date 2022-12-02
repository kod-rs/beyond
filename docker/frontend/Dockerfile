# syntax=docker/dockerfile:1
FROM ubuntu:22.04

RUN DEBIAN_FRONTEND=noninteractive DEBCONF_NOWARNINGS=yes apt-get update -y
RUN DEBIAN_FRONTEND=noninteractive DEBCONF_NOWARNINGS=yes apt-get install -y nodejs npm

ADD src_front src_front
COPY run_frontend.sh src_front/run_frontend.sh

WORKDIR src_front

RUN npm install

EXPOSE 3000

CMD ["./run_frontend.sh"]
