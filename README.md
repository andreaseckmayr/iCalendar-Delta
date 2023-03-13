# iCalendar-Delta

## Usage

### Docker Compose

| ------------- | ----------------------------------------------- |
| Parameter     | Function                                        |
| ------------- | ----------------------------------------------- |
| -v /config    | location for calendar config, cron files, nginx |
| -v /calendars | location for created calendars                  |
| ------------- | ----------------------------------------------- |

```/bin/bash
docker compose up -d
```

## Build

```/bin/bash
docker compose build
```
