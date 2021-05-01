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
        if 1 <= day <= 31:
            self._day = day
        else:
            print("Invalid value entered for day: " + day)

    def set_month(self, month):
        if 1 <= month <= 12:
            self._month = month
        else:
            print("Invalid value entered for month: " + month)

    def set_year(self, year):
        if 1900 <= year <= 3000:
            self._year = year
        else:
            print("Invalid value entered for year: " + year)

    def get_day(self):
        return self._day

    def get_month(self):
        return self._month

    def get_year(self):
        return self._year

