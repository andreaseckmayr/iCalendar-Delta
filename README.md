# iCalendar-Delta

Purpose of this app is to load two or more calendars and create a new calendar with events which are missing in the main calendar. So if two persons have almost the same events, you can create a calendar with all events that you don't but the other person does have scheduled. This allows you to see if the other person is free without having a crowded timeline.

## Usage

### Deploy with Docker Compose

| Parameter     | Function                                        |
| ------------- | ----------------------------------------------- |
| -v /config    | location for calendar config, cron files, nginx |
| -v /calendars | location for created calendars                  |

```/bin/bash
docker compose up -d
```

### Update

```/bin/bash
docker compose pull && docker compose up -d --force-recreate
```

### Clean up

```/bin/bash
docker image prune
```

## Build

```/bin/bash
docker compose build
```

### Push to Quay.io

```/bin/bash
docker push quay.io/andreaseckmayr/ical-delta/app:latest
```

```/bin/bash
docker push quay.io/andreaseckmayr/ical-delta/web:latest
```
