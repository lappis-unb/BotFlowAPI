FROM debian:buster-slim

EXPOSE 8000

RUN apt-get update && apt-get install -y --no-install-recommends \
        python3 \
        python3-pip \
        python3-crypto \
        python3-pyodbc \
        python3-setuptools

RUN pip3 install --no-cache-dir toolz

RUN mkdir src

COPY src/ src/

COPY requirements.txt requirements.txt

COPY runserver.sh runserver.sh

COPY tox.ini tox.ini

RUN pip3 install -r requirements.txt

