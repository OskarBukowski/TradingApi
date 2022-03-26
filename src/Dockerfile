FROM python:3.8-slim-buster

COPY requirements.txt /home/api/requirements.txt

RUN pip install -r /home/api/requirements.txt

RUN mkdir -p /home/api

COPY . /home/api

CMD ["/bin/bash", "/home/api/run.sh"]