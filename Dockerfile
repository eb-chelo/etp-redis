FROM redis

ENV SHELL=/bin/bash

RUN apt-get update && apt-get -y install vim \
    && mkdir /volumes
RUN apt-get install pipenv
COPY replication /volumes/replication
VOLUME /volumes
