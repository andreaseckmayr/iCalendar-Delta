FROM ubuntu:22.04

RUN apt-get update && apt-get install -y python3 python3-pip cron

WORKDIR /

ADD ./app/ical_delta.py .
ADD ./app/requirements.txt .

RUN pip install -r requirements.txt

ADD ./app/crontabfile /app/crontab
RUN chmod 0644 /app/crontab
RUN crontab /app/crontab

#CMD [ "cron", "-f" ]

ADD ./app/exec.sh .
RUN chmod +x exec.sh

ENTRYPOINT [ "/bin/bash", "exec.sh" ]