class TimeSpan:
    _hour = 0
    _minute = 0

    def __init__(self, hour, minute):
        self.set_hour(hour)
        self.set_minute(minute)

    def __str__(self):
        string = str(self._hour) + ":" + str(self._minute).zfill(2)
        return string

    def __add__(self, other):
        hour = 0
        minute = self.get_minute() + other.get_minute()

        if minute >= 60:
            minute -= 60
            hour += 1

        hour += self.get_hour() + other.get_hour()

        return TimeSpan(hour,minute)

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
