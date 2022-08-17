# syntax=docker/dockerfile:1
FROM ubuntu:22.04
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update
RUN apt-get install -y postgresql postgresql-contrib
RUN localedef -i en_US -f UTF-8 en_US.UTF-8
RUN localedef -i hr_HR -f UTF-8 hr_HR.UTF-8

ADD run_psql.sh run_psql.sh
COPY --chown=postgres run_psql.sh run_psql.sh
COPY var_lib_psql_14_main /var/lib/postgresql/14/main
COPY etc_psql_14 /etc/postgresql/14
COPY usr_lib_psql_14 /usr/lib/postgresql/14

RUN echo "host all  all    0.0.0.0/0  md5" >> /etc/postgresql/14/main/pg_hba.conf
RUN echo "listen_addresses='*'" >> /etc/postgresql/14/main/postgresql.conf

EXPOSE 5432

USER postgres
CMD ["./run_psql.sh"]
