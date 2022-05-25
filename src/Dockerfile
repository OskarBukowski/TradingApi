FROM python:3.8-slim-buster

MAINTAINER OskarBukowski

RUN addgroup docker && adduser --no-create-home --disabled-password --ingroup docker docker


RUN mkdir -p /home/api

COPY requirements.txt /home/api/requirements.txt

RUN pip install -r /home/api/requirements.txt

COPY . /home/api

USER docker

CMD ["echo", "Starting TradingApi script"]

ENTRYPOINT ["/bin/bash", "/home/api/run.sh"]