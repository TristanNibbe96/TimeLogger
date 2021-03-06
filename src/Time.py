from TimeSpan import TimeSpan
import enum
import copy


class Meridian(enum.Enum):
    AM = 1
    PM = 2

    def __str__(self):
        return self.name


class Time:
    _hour = 0
    _minute = 0
    _meridian = Meridian.AM

    def __init__(self, hour, minute, meridian):
        self.set_hour(hour)
        self.set_minute(minute)
        self.set_meridian(meridian)

    def __sub__(end, start):
        interval: TimeSpan
        hour = 0
        minute = 0
        start_counter = copy.deepcopy(start)

        if end.get_minute() > start.get_minute():
            minute = end.get_minute() - start.get_minute()
        elif end.get_minute() < start.get_minute():
            end.decrement_hour()
            minute = 60
            while start_counter.get_minute() != end.get_minute():
                minute -= 1
                start_counter.decrement_minute()

        while start_counter.get_hour() != end.get_hour():
            start_counter.increment_hour()
            hour += 1

        interval = TimeSpan(hour, minute)

        return interval

    def __eq__(self, other):
        equal = True
        if self.get_hour() != other.get_hour():
            equal = False
        if self.get_minute() != other.get_minute():
            equal = False
        if self.get_meridian() != other.get_meridian():
            equal = False

        return equal

    def __copy__(self):
        copy = Time(self.get_hour(), self.get_minute(), self.get_meridian())
        return copy

    def __str__(self):
        string = str(self._hour) + ":" + str(self._minute).zfill(2) + str(self._meridian)
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

    def set_meridian(self, meridian):
        if type(meridian) != Meridian:
            print("Invalid AM variable: " + str(meridian))
        else:
            self._meridian = meridian

    def get_minute(self):
        return self._minute

    def get_hour(self):
        return self._hour

    def get_meridian(self):
        return self._meridian

    def increment_hour(self):
        if self.get_hour() == 12:
            self.set_hour(1)
        else:
            new_hour = self.get_hour() + 1
            self.set_hour(new_hour)

    def decrement_hour(self):
        if self.get_hour() == 1:
            self.set_hour(12)
        else:
            new_hour = self.get_hour() - 1
            self.set_hour(new_hour)

    def decrement_minute(self):
        if self.get_minute() == 0:
            self.set_minute(59)
        else:
            new_minute = self.get_minute() - 1
            self.set_minute(new_minute)
