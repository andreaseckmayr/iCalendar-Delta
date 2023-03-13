#!/bin/bash
while true; do
  python3 ical_delta.py > ical_delta.log
  sleep 600
done