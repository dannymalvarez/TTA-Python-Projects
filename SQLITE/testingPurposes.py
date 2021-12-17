
'''
The Portland-based company you work for just opened
two new branches. One is in New York City,
the other in London. They need a very simple program
to find out if the branches are open or closed.
The hours of both branches are 9:00 a.m.-5:00 p.m.
in their own time zone.

Create a script that will find out the current
times in the Portland HQ and NYC and London branches.

Then, compare that time with each branch's hours
to see if they are open or closed.

Print out to the screen the three branches
and whether they are open or closed.
'''
import datetime
from datetime import datetime
import pytz


london_tz = pytz.timezone('Europe/London')
now_london = datetime.now(tz=london_tz)
time_london = now_london.strftime("%I:%M:%p")
print("The time in London is currently: ", time_london, "\nOperating hours are between 9:00 AM and 5:00 PM")
london_hour = int(now_london.strftime("%H"))
if london_hour > 9 and london_hour < 17:
    print("The London branch is open!")
else:
    print("The London branch is currently closed.")
print('\n')

portland_tz = pytz.timezone('US/Pacific')
now_portland = datetime.now(tz=portland_tz)
time_portland = now_portland.strftime("%I:%M:%p")
print("The time in Portland is currently: ", time_portland, "\nOperating hours are between 9:00 AM and 5:00 PM")
portland_hour = int(now_portland.strftime("%H"))
if portland_hour > 9 and portland_hour < 17:
    print("The Portland branch is open!")
else:
    print("The Portland branch is currently closed.")
print('\n')

ny_tz = pytz.timezone('America/New_York')
now_ny = datetime.now(tz=ny_tz)
time_ny = now_ny.strftime("%I:%M:%p")
print("The time in New York is currently: ", time_ny, "\nOperating hours are between 9:00 AM and 5:00 PM")
ny_hour = int(now_ny.strftime("%H"))
if ny_hour > 9 and ny_hour < 17:
    print("The New York branch is open!")
else:
    print("The New York branch is currently closed.")
