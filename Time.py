class Time:
    _hour = 0
    _minute = 0
    _am = True

    def __init__(self, hour, minute, AM):
        self.set_hour(hour)
        self.set_minute(minute)
        self.set_am(AM)

    def __sub__(self, other):
        return self.get_minute() - other.get_minute()

    def set_hour(self, hour):
        self._hour = hour

    def set_minute(self, minute):
        self._minute = minute

    def set_am(self, am):
        self._am = am

    def get_minute(self):
        return self._minute

    def get_hour(self):
        return self._hour

    def get_am(self):
        return self._am
