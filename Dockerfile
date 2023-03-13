FROM ubuntu:latest

RUN apt-get update && apt-get install -y python3 python3-pip cron

WORKDIR /calendars
ADD ical_delta.py .
ADD requirements.txt .

RUN pip install -r requirements.txt

RUN echo '* * * * * python3 /calendar/ical_delta.py' > /etc/crontab

ENTRYPOINT [ "cron", "-f" ]