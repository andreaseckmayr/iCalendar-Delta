'''
python: 3.11
2023-03-13
A. Eckmayr
'''

# %%  load dependencies
from typing import Set
import os
import csv
from datetime import datetime
from icalendar import Calendar
import urllib3


# %%
class ICalWrapper:
    '''
    class provides basic funtionality for loading and storing ical objects
    '''
    def __init__(self, url: str, name: str, uid: str):
        self.url = url
        self.name = name
        self.uid = uid
        self.cal = None
        self.uids = None

    def load_from_url(self) -> Calendar:
        '''load calendar from url'''
        http = urllib3.PoolManager()
        req = http.request('GET', self.url)
        self.cal = Calendar.from_ical(req.data)
        req.close()
        return self.cal

    def get_uids(self) -> Set[str]:
        '''get uids from calendar entries as set'''
        uids = []
        for comp in self.cal.walk():
            if comp.name == 'VEVENT':
                uids.append(comp.get('uid'))
        self.uids = set(uids)
        return self.uids

    def __str__(self):
        return f'{self.url}'


# %%
def compare(a: ICalWrapper, b: ICalWrapper) -> Calendar:
    '''
    take two calendars and return a new cal with missing entries
    '''
    cal = Calendar()
    cal.add('prodid', f"{a.name}//ndrs.dev")
    cal.add('version', '1.0')
    for comp in b.cal.walk():
        if comp.name == 'VEVENT':
            if comp.get('uid') not in a.uids:
                cal.add_component(comp)
    return cal


# %%  set static urls
calendars = {}
with open('/config/calendars.csv', 'r', encoding='UTF-8') as file:
    csv_reader = csv.reader(file, delimiter=';')
    for row in csv_reader:
        calendars[row[0]] = ICalWrapper(row[1], row[2], row[3])

# %%  load calendars
for _, item in calendars.items():
    item.load_from_url()
    item.get_uids()

# %%  compare calendars and add missing events
cal_a_delta = compare(calendars['1'], calendars['2'])
cal_b_delta = compare(calendars['2'], calendars['1'])

# %%  write calendars to file
with open(os.path.join('/calendars', f'{calendars["1"].uid}.ics'), 'wb') as f:
    f.write(cal_a_delta.to_ical())

with open(os.path.join('/calendars', f'{calendars["2"].uid}.ics'), 'wb') as f:
    f.write(cal_b_delta.to_ical())

# %%
print(f'{datetime.now()}: cal sync completed')
