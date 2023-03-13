FROM ubuntu:latest

RUN apt-get update && apt-get install -y python3 python3-pip cron

WORKDIR /calendars
ADD ical_delta.py .

RUN echo '*/5 * * * * ical_delta.py' > /etc/crontab

ENTRYPOINT [ "cron", "-f" ]