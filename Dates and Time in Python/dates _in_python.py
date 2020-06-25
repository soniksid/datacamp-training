# importing packages
import pandas as pd
from datetime import timedelta, datetime, timezone, date
from dateutil import tz 


# printing year from date objct
list1 = [date(2016, 10, 25), date(2000, 7, 21)]
print("year is", list1[1].year)


# counting no. of days upto 200 days from 21-07-2020 
d1 = date(2020, 7, 21)
td = timedelta(days = 200)
print("Date after 200 days from 21st July 2020 is:", d1 + td)


# timezones
EDT = timezone(timedelta(hours = -7))
dt = datetime(2020, 6, 19, 2, 38, 10, tzinfo = EDT)
IST = timezone(timedelta(hours = 5, minutes = 30))
print("The time in India is", dt.astimezone(IST), "when time in California was ", dt.astimezone(EDT))


# code to find timezone
IST1 = tz.gettz('Asia/Kolkata')
date = datetime(2020, 6, 19, 15, 49, 10, tzinfo = IST1)
print(date)


# reading dates from csv files
df = pd.read_csv('AirQuality.csv', parse_dates = ['lastupdate'])
print(df['lastupdate'].head(5))

