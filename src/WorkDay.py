from TimeSpan import TimeSpan
from DateTime import DateTime
from TimeInterval import TimeInterval
from Date import Date


class WorkDay:
    _intervals = []
    _current_interval_start = None
    date = None

    def __str__(self):
        work_day_string = str(self.date)
        work_day_string += "\n\n"
        for interval in self._intervals:
            work_day_string += str(interval)
            work_day_string += "\n\n"
        work_day_string += "Hours Worked: " + str(self.get_total_hours_worked())
        return work_day_string

    def end_current_interval(self, end_datetime):
        new_interval = TimeInterval(self._current_interval_start, end_datetime)
        self.append_interval(new_interval)
        self._current_interval_start = None

    def set_interval_start(self, start_datetime):
        self._current_interval_start = start_datetime
        if self.date is None:
            self.date = start_datetime.get_date()

    def get_total_hours_worked(self):
        self.check_for_incomplete_interval()
        total = TimeSpan(0, 0)
        for interval in self._intervals:
            total += interval.get_interval()
        return total

    def append_interval(self, interval):
        self._intervals.append(interval)

    def clear_interval(self):
        self._intervals = []

    def check_for_incomplete_interval(self):
        hanging_interval = False
        if self._current_interval_start is not None:
            hanging_interval = True

        if hanging_interval:
            print("Trying to access total hours worked in a day that has an incomplete time interval")

        return hanging_interval
