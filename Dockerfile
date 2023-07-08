FROM python:3

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
