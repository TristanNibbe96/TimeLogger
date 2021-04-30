class DateTime:

    def __init__(self, date, time):
        self.set_date(date)
        self.set_time(time)

    def set_date(self, date):
        self.date = date

    def set_time(self, time):
        self.time = time
