FROM python:3
ENV PYTHONUNBUFFERED=1

EXPOSE 8000

RUN mkdir src

COPY src/ src/

COPY requirements.txt requirements.txt

COPY runserver.sh runserver.sh

RUN pip3 install -r requirements.txt