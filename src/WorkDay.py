from TimeInterval import TimeInterval
from DateTime import DateTime


class WorkDay:
    _intervals: TimeInterval
    _current_interval_start: DateTime

    def set_interval_start(self,interval):
        self._current_interval_start = interval
