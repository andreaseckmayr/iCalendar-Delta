FROM ubuntu:latest

RUN apt-get update && apt-get install -y python3 python3-pip cron

WORKDIR /calendars
ADD ical_delta.py .
ADD ical_serve.py .
ADD requirements.txt .

RUN pip install -r requirements.txt

RUN echo '*/5 * * * * ical_delta.py' > /etc/crontab

ENV FLASK_APP=ical_serve.py
ENV FLASK_DEBUG=1

ENTRYPOINT [ "cron", "-f" ]

#CMD flask run --host 0.0.0.0