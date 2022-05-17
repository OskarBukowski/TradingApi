FROM python:3.8-slim-buster

RUN addgroup docker && adduser --no-create-home --disabled-password --ingroup docker docker

USER docker

RUN mkdir -p /home/api

COPY requirements.txt /home/api/requirements.txt

RUN pip install -r /home/api/requirements.txt

COPY . /home/api

CMD ["/bin/bash", "/home/api/run.sh"]