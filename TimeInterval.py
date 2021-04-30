from DateTime import DateTime


class TimeInterval:
    _start: DateTime
    _end: DateTime

    def __init__(self, start, end):
        self._start = start
        self._end = end

    def get_interval(self):
        interval = 0

        if self._start.date == self._end.date:
            return self._end.time - self._start.time
        else:
            print("DateTimes for this interval are on two different days")
        return interval
