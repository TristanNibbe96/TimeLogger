class TimeSpan:
    _hour = 0
    _minute = 0

    def __init__(self, hour, minute):
        self.set_hour(hour)
        self.set_minute(minute)

    def __str__(self):
        string = str(self._hour) + ":" + str(self._minute)
        return string

    def set_hour(self, hour):
        if 0 <= hour <= 23:
            self._hour = hour
        else:
            print("Invalid hour entered: " + str(hour))

    def set_minute(self, minute):
        if 0 <= minute <= 59:
            self._minute = minute
        else:
            print("Invalid minute entered: " + str(minute))

    def get_minute(self):
        return self._minute

    def get_hour(self):
        return self._hour


class Time:
    _hour = 0
    _minute = 0
    _am = True

    def __init__(self, hour, minute, am):
        self.set_hour(hour)
        self.set_minute(minute)
        self.set_am(am)

    def __sub__(self, other):
        interval: TimeSpan
        hour = 0
        minute = 0

        if self.get_am() == other.get_am():
            hour = self.get_hour() - other.get_hour()
            minute = self.get_minute() - other.get_minute()

        interval = TimeSpan(hour, minute)

        return interval

    def __str__(self):
        string = str(self._hour) + ":" + str(self._minute) + str(self._am)
        return string

    def set_hour(self, hour):
        if 1 <= hour <= 12:
            self._hour = hour
        else:
            print("Invalid hour entered: " + str(hour))

    def set_minute(self, minute):
        if 0 <= minute <= 59:
            self._minute = minute
        else:
            print("Invalid minute entered: " + str(minute))

    def set_am(self, am):
        if type(am) != bool:
            print("Invalid AM variable: " + str(am))
        else:
            self._am = am

    def get_minute(self):
        return self._minute

    def get_hour(self):
        return self._hour

    def get_am(self):
        return self._am
