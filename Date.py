class Date:
    _day = 0
    _month = 0
    _year = 0

    def __init__(self, day, month, year):
        self.set_year(year)
        self.set_month(month)
        self._day(day)

    def set_day(self, day):
        self._day = day

    def set_month(self, month):
        self._month = month

    def set_year(self, year):
        self._year = year
