# -*- coding: utf-8 -*-
import getpass

def get_username():
    return getpass.getuser()
##Get the time and determine phase of day:

from datetime import datetime

# Define when certain day phases begin
EVENING = 18
AFTERNOON = 12

def get_day_phase(time_now):
    hour_of_day = time_now.hour
    if hour_of_day > EVENING:
        return 'Evening'
    elif hour_of_day > AFTERNOON:
        return 'Afternoon'
    else:
        return 'Morning'
##Get the date and time (in a pretty format):

def get_pretty_datetime(now):
    return now.strftime('[%d, %b %Y | %H:%M]') # e.g [09, Oct 2017 | 16:09]
##Now to mix it all together!

now = datetime.now()
print(get_pretty_datetime(now), 'Good', get_day_phase(now), get_username() )