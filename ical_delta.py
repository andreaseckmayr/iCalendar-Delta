'''
python: 3.11
2023-03-13
A. Eckmayr
'''

# %%  load dependencies
from icalendar import Calendar, Event
from datetime import datetime
from pytz import UTC
import urllib3

# %%
def get_uids(cal):
    uids = []
    for comp in cal.walk():
        if comp.name == 'VEVENT':
            uids.append(comp.get('uid'))
            #print(comp.get('summary'))
    return set(uids)

# %%  set static urls
CAL_A = 'http://stundenplan.fh-ooe.at/ics/bd6e177711f7462078.ics'
CAL_B = 'http://stundenplan.fh-ooe.at/ics/8d8b8670dd17493b79.ics'

# %%  load first calendar
http = urllib3.PoolManager()
r = http.request('GET', CAL_A)
cal_a = Calendar.from_ical(r.data)
r.close()
uids_a = get_uids(cal_a)

# %%  load second calendar
r = http.request('GET', CAL_B)
cal_b = Calendar.from_ical(r.data)
r.close()
uids_b = get_uids(cal_b)

# %%  compare calendars and add missing events
delta_a = uids_a.difference(uids_b)
delta_b = uids_b.difference(uids_a)

cal_a_delta = Calendar()
cal_a_delta.add('prodid', 'fhooe-dse-andreas//ndrs.dev')
cal_a_delta.add('version', '1.0')

cal_b_delta = Calendar()
cal_b_delta.add('prodid', 'fhooe-dse-magdalena//ndrs.dev')
cal_b_delta.add('version', '1.0')

for comp in cal_b.walk():
    if comp.name == 'VEVENT':
        if comp.get('uid') not in uids_a:
            cal_a_delta.add_component(comp)

for comp in cal_a.walk():
    if comp.name == 'VEVENT':
        if comp.get('uid') not in uids_b:
            cal_b_delta.add_component(comp)

# %%  write calendars to file
f = open('andreas_delta.ics', 'wb')
f.write(cal_a_delta.to_ical())
f.close()

f = open('magdalena_delta.ics', 'wb')
f.write(cal_b_delta.to_ical())
f.close()

# %%
print('cal sync completed')
