FROM python:3.8-slim-buster

RUN mkdir -p /home/api

COPY requirements.txt /home/api/requirements.txt

RUN pip install -r /home/api/requirements.txt

COPY . /home/api