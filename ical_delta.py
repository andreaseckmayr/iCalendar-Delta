'''
python: 3.11
2023-03-13
A. Eckmayr
'''

# %%  load dependencies
from typing import Set
from icalendar import Calendar, Event
from datetime import datetime
from pytz import UTC
import urllib3
import os
import datetime
import csv

# %%
class Cal:
    def __init__ (self, url: str, name: str, hash: str):
        self.url = url
        self.name = name
        self.hash = hash
    
    def __str__(self):
        return f'{self.url}'

# %%
def get_cal(url: str) -> Calendar:
    '''load calendar from url'''
    http = urllib3.PoolManager()
    r = http.request('GET', url)
    cal = Calendar.from_ical(r.data)
    r.close()
    return cal

# %%
def get_uids(cal: Calendar) -> Set[str]:
    '''get uids from calendar entries as set'''
    uids = []
    for comp in cal.walk():
        if comp.name == 'VEVENT':
            uids.append(comp.get('uid'))
            #print(comp.get('summary'))
    return set(uids)

# %%
def compare(a: Cal, b: Cal) -> Calendar:
    '''take two calendars and return a new cal with missing entries'''
    cal = Calendar()
    cal.add('prodid', f"{a.name}//ndrs.dev")
    cal.add('version', '1.0')
    for comp in b.cal.walk():
        if comp.name == 'VEVENT':
            if comp.get('uid') not in a.uids:
                cal.add_component(comp)
    return cal

# %%  set static urls
calendars = dict()
with open('/config/calendars.csv', 'r') as file:
    csv_reader = csv.reader(file, delimiter=';')
    for row in csv_reader:
        calendars[row[0]] = Cal(row[1], row[2], row[3])

# %%  load calendars
for _, item in calendars.items():
    c = get_cal(item.url)
    item.cal = c
    item.uids = get_uids(c)

# %%  compare calendars and add missing events
cal_a_delta = compare(calendars['1'], calendars['2'])
cal_b_delta = compare(calendars['2'], calendars['1'])

# %%  write calendars to file
f = open(os.path.join('/calendars', f'{calendars["1"].hash}.ics'), 'wb')  # $ echo -n andreas | md5sum -> andreas
f.write(cal_a_delta.to_ical())
f.close()

f = open(os.path.join('/calendars', f'{calendars["2"].hash}.ics'), 'wb')  # magdalena
f.write(cal_b_delta.to_ical())
f.close()

# %%
print(f'{datetime.datetime.now()}: cal sync completed')
