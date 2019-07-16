FROM redis

ENV SHELL=/bin/bash

EXPOSE 5000

RUN apt-get update && apt-get -y install vim \
    && mkdir /volumes
RUN apt-get -y install pipenv
COPY replication /volumes/replication
COPY examples /volumes/examples
VOLUME /volumes
