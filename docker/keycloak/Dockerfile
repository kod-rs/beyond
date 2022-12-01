# syntax=docker/dockerfile:1
FROM ubuntu:22.04

ENV DEBIAN_FRONTEND noninteractive

WORKDIR .

RUN apt-get update
RUN apt-get install -y default-jre

ADD keycloak-19.0.3 keycloak-19.0.3
COPY run_keycloak.sh run_keycloak.sh

EXPOSE 8080

CMD ["./run_keycloak.sh"]