import unittest
from src.TimeInterval import TimeInterval
from src.Time import Time
from src.Time import Meridian
from src.Date import Date
from src.DateTime import DateTime


class TestTimeSubtraction(unittest.TestCase):

    def test_minutes_less_than(self):
        time_one = Time(12, 40, Meridian.PM)
        time_two = Time(5, 30, Meridian.PM)

        date_one = Date(4, 29, 2021)
        date_two = Date(4, 29, 2021)

        date_time_one = DateTime(date_one, time_one)
        date_time_two = DateTime(date_two, time_two)

        interval = TimeInterval(date_time_one, date_time_two)

        self.assertEqual(str(interval.get_interval()), "4:10")


if __name__ == '__main__':
    unittest.main()
