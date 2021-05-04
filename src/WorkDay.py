from xxlimited import Null
from TimeInterval import TimeInterval
from DateTime import DateTime


class WorkDay:
    _intervals: TimeInterval
    _current_interval_start: DateTime

    def set_interval_start(self,interval):
        self._current_interval_start = interval

    def get_total_hours_worked(self):
        self.check_for_incomplete_interval()
        total = 0
        #for interval in interval
        #total += interval
        return total


    def check_for_incomplete_interval(self):
        if self._current_interval_start != Null:
            print("Trying to access total hours worked in a day that has an incomplete time interval")
