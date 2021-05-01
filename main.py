from TimeInterval import TimeInterval
from Time import Time
from Time import Meridian
from Date import Date
from DateTime import DateTime

time_one = Time(12, 0, Meridian.PM)
time_two = Time(5, 0, Meridian.PM)

date_one = Date(4, 29, 2021)
date_two = Date(4, 29, 2021)

date_time_one = DateTime(date_one, time_one)
date_time_two = DateTime(date_two, time_two)

interval = TimeInterval(date_time_one, date_time_two)

print(interval.get_interval())

