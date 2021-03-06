from Date import Date
from Time import Time


class DateTime:

    date: Date
    time: Time

    def __init__(self, date, time):
        self.set_date(date)
        self.set_time(time)

    def set_date(self, date):
        self.date = date

    def set_time(self, time):
        self.time = time

    def get_time(self):
        return self.time

    def get_date(self):
        return self.date
