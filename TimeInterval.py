class TimeInterval:
    _start = 0
    _end = 0

    def __init__(self, start, end):
        self._start = start
        self._end = end

    def get_interval(self):
        interval = 0
        if self._start.date == self._end.date:
            self._start.time.difference(self._end.time)
        else:
            print("DateTimes for this interval are on two different days")
        return interval







