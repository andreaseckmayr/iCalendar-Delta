FROM ubuntu:22.04

RUN apt-get update && apt-get install -y python3 python3-pip cron

WORKDIR /

ADD ./ical_delta.py .
ADD ./requirements.txt .

RUN pip install -r requirements.txt

ADD ./crontabfile /app/crontab
RUN chmod 0644 /app/crontab
RUN crontab /app/crontab

#CMD [ "cron", "-f" ]

ADD ./exec.sh .
RUN chmod +x exec.sh

ENTRYPOINT [ "/bin/bash", "exec.sh" ]