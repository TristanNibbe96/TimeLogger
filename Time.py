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
        if 1 <= hour <= 12:
            self._hour = hour
        else:
            print("Invalid hour entered: " + hour)

    def set_minute(self, minute):
        if 0 <= minute <= 59:
            self._minute = minute
        else:
            print("Invalid minute entered: " + minute)

    def set_am(self, am):
        if type(am) != bool:
            print("Invalid AM variable: " + am)
        else:
            self._am = am

    def get_minute(self):
        return self._minute

    def get_hour(self):
        return self._hour

    def get_am(self):
        return self._am
