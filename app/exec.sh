#!/bin/bash
while true; do
  python3 -u ical_delta.py > ical_delta.log
  sleep 600
done
