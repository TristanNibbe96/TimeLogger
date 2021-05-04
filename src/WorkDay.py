from xxlimited import Null
from TimeSpan import TimeSpan
from DateTime import DateTime


class WorkDay:
    _intervals = []
    _current_interval_start: DateTime

    def set_interval_start(self,interval):
        self._current_interval_start = interval

    def get_total_hours_worked(self):
        self.check_for_incomplete_interval()
        total = TimeSpan(0, 0)
        for interval in self._intervals:
            total += interval.get_interval()
        return total

    def append_interval(self,interval):
        self._intervals.append(interval)

    def check_for_incomplete_interval(self):
        if self._current_interval_start != Null:
            print("Trying to access total hours worked in a day that has an incomplete time interval")
