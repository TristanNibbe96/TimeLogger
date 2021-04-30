class Time:
    _hour = 0
    _minute = 0
    _am = True

    def __init__(self, hour, minute, AM):
        self.set_hour(hour)
        self.set_minute(minute)
        self.set_am(AM)

    def set_hour(self, hour):
        self._hour = hour

    def set_minute(self, minute):
        self._minute = minute

    def set_am(self, am):
        self._am = am
