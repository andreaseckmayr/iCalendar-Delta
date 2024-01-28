FROM python:alpine
#FROM ubuntu:22.04

RUN apk update && apk upgrade

RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools

#RUN apt-get update && apt-get upgrade -y && apt-get install -y \
#    python3 \
#    python3-pip \
#    cron \
#    ncat \
#    && rm -rf /var/lib/apt/lists/*

WORKDIR /

ADD ./ical_delta.py .
ADD ./requirements.txt .

RUN pip install -r requirements.txt

#ADD ./crontabfile /app/crontab
#RUN chmod 0644 /app/crontab
#RUN crontab /app/crontab

#CMD [ "cron", "-f" ]

ADD ./exec.sh .
RUN chmod +x exec.sh

ENTRYPOINT [ "/bin/sh", "exec.sh" ]