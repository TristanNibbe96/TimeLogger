class Date:
    _day = 0
    _month = 0
    _year = 0

    def __init__(self, month, day, year):
        self.set_year(year)
        self.set_month(month)
        self.set_day(day)

    def __str__(self):
        string = str(self.get_month()) + "/" + str(self.get_day()) + "/" + str(self.get_year())
        return string

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
            print("Invalid value entered for day: " + str(day))

    def set_month(self, month):
        if 1 <= month <= 12:
            self._month = month
        else:
            print("Invalid value entered for month: " + str(month))

    def set_year(self, year):
        if 1900 <= year <= 3000:
            self._year = year
        else:
            print("Invalid value entered for year: " + str(year))

    def get_day(self):
        return self._day

    def get_month(self):
        return self._month

    def get_year(self):
        return self._year

