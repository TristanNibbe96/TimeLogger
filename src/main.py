from TimeInterval import TimeInterval
from Time import Time
from Time import Meridian
from Date import Date
from DateTime import DateTime
from WorkDay import WorkDay

day = WorkDay()
day.clear_interval()

time_one = Time(12, 30, Meridian.PM)
time_two = Time(2, 30, Meridian.PM)

date_one = Date(4, 29, 2021)
date_two = Date(4, 29, 2021)

date_time_one = DateTime(date_one, time_one)
date_time_two = DateTime(date_two, time_two)

day.set_interval_start(date_time_one)
day.end_current_interval(date_time_two)

time_one = Time(2, 30, Meridian.PM)
time_two = Time(4, 30, Meridian.PM)

date_time_one = DateTime(date_one, time_one)
date_time_two = DateTime(date_two, time_two)

day.set_interval_start(date_time_one)
day.end_current_interval(date_time_two)

print(str(day))

