import unittest
from Time import Time
from Time import Meridian
from Date import Date
from DateTime import DateTime
from WorkDay import WorkDay


class TestSingleInterval(unittest.TestCase):

    def test_single_interval_calculation(self):
        day = WorkDay()

        time_one = Time(12, 40, Meridian.PM)
        time_two = Time(5, 30, Meridian.PM)

        date_one = Date(4, 29, 2021)
        date_two = Date(4, 29, 2021)

        date_time_one = DateTime(date_one, time_one)
        date_time_two = DateTime(date_two, time_two)

        day.set_interval_start(date_time_one)
        day.end_current_interval(date_time_two)

        self.assertEqual(str(day.get_total_hours_worked()), "4:50")


if __name__ == '__main__':
    unittest.main()