class Date:
    _day = 0
    _month = 0
    _year = 0

    def __init__(self, day, month, year):
        self.set_year(year)
        self.set_month(month)
        self.set_day(day)

    def __eq__(self, other):
        equal = True
        if self.get_day() != other.get_day():
            equal = False
        if self.get_month() != other.get_month():
            equal = False
        if self.get_year() != other.get_year():
            equal = False

        return equal

    def set_day(self, day):
        self._day = day

    def set_month(self, month):
        self._month = month

    def set_year(self, year):
        self._year = year

    def get_day(self):
        return self._day

    def get_month(self):
        return self._month

    def get_year(self):
        return self._year

