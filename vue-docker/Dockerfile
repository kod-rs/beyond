# syntax=docker/dockerfile:1
FROM ubuntu:22.04

ENV DEBIAN_FRONTEND noninteractive

WORKDIR .

RUN apt-get update
RUN apt-get install -y nodejs npm

ADD src src
COPY package.json package.json
COPY vue.config.js vue.config.js
COPY webpack.config.js webpack.config.js
COPY run_vue.sh run_vue.sh

EXPOSE 3000

RUN npm install
CMD ["./run_vue.sh"]
