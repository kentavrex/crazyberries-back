FROM  docker-registry.selectel.ru/library/python:3.10-buster

ADD requirements.txt /cb/

WORKDIR /cb

RUN apt-get update ; \
    apt-get install -y \
        postgresql-server-dev-all \
        python3-dev \
    && pip install --upgrade pip \
    && pip install -r requirements.txt \
    && rm requirements.txt

ADD . /cb

EXPOSE 5000

USER cb
