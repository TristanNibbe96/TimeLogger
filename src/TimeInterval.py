from DateTime import DateTime


class TimeInterval:
    _start: DateTime
    _end: DateTime

    def __init__(self, start, end):
        self._start = start
        self._end = end

    def __str__(self):
        string = "Start: " + str(self._start.get_time())
        string += "\nEnd: " + str(self._end.get_time())

        return string

    def get_interval(self):
        interval = 0

        if self._start.get_date() == self._end.get_date():
            return self._end.get_time() - self._start.get_time()
        else:
            print("DateTimes for this interval are on two different days")
        return interval
