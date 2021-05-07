import unittest
from Time import Time
from Time import Meridian
from Date import Date
from DateTime import DateTime
from WorkDay import WorkDay


class TestSingleInterval(unittest.TestCase):

    def test_single_interval_calculation(self):
        day = WorkDay()
        day.clear_interval()

        time_one = Time(12, 40, Meridian.PM)
        time_two = Time(5, 30, Meridian.PM)

        date_one = Date(4, 29, 2021)
        date_two = Date(4, 29, 2021)

        date_time_one = DateTime(date_one, time_one)
        date_time_two = DateTime(date_two, time_two)

        day.set_interval_start(date_time_one)
        day.end_current_interval(date_time_two)

        self.assertEqual(str(day.get_total_hours_worked()), "4:50")

    def test_single_interval_not_hanging(self):
        day = WorkDay()
        day.clear_interval()

        time_one = Time(12, 40, Meridian.PM)
        time_two = Time(5, 30, Meridian.PM)

        date_one = Date(4, 29, 2021)
        date_two = Date(4, 29, 2021)

        date_time_one = DateTime(date_one, time_one)
        date_time_two = DateTime(date_two, time_two)

        day.set_interval_start(date_time_one)
        day.end_current_interval(date_time_two)

        self.assertEqual(day.check_for_incomplete_interval(), False)

    def test_single_interval_hanging(self):
        day = WorkDay()
        day.clear_interval()

        time_one = Time(12, 40, Meridian.PM)
        date_one = Date(4, 29, 2021)
        date_time_one = DateTime(date_one, time_one)

        day.set_interval_start(date_time_one)

        self.assertEqual(day.check_for_incomplete_interval(), True)


class TestMultipleIntervals(unittest.TestCase):

    def test_multiple_interval_calculation(self):
        day = WorkDay()
        day.clear_interval()

        time_one = Time(12, 30, Meridian.PM)
        time_two = Time(2, 30, Meridian.PM)

        date_one = Date(4, 29, 2021)
        date_two = Date(4, 29, 2021)

        date_time_one = DateTime(date_one, time_one)
        date_time_two = DateTime(date_two, time_two)

        day.set_interval_start(date_time_one)
        day.end_current_interval(date_time_two)

        time_one = Time(2, 30, Meridian.PM)
        time_two = Time(4, 30, Meridian.PM)

        date_time_one = DateTime(date_one, time_one)
        date_time_two = DateTime(date_two, time_two)

        day.set_interval_start(date_time_one)
        day.end_current_interval(date_time_two)

        self.assertEqual(str(day.get_total_hours_worked()), "4:00")

    def test_multiple_interval_not_hanging(self):
        day = WorkDay()
        day.clear_interval()

        time_one = Time(12, 30, Meridian.PM)
        time_two = Time(2, 30, Meridian.PM)

        date_one = Date(4, 29, 2021)
        date_two = Date(4, 29, 2021)

        date_time_one = DateTime(date_one, time_one)
        date_time_two = DateTime(date_two, time_two)

        day.set_interval_start(date_time_one)
        day.end_current_interval(date_time_two)

        time_one = Time(2, 30, Meridian.PM)
        time_two = Time(4, 30, Meridian.PM)

        date_time_one = DateTime(date_one, time_one)
        date_time_two = DateTime(date_two, time_two)

        day.set_interval_start(date_time_one)
        day.end_current_interval(date_time_two)

        self.assertEqual(day.check_for_incomplete_interval(), False)

    def test_multiple_interval_hanging(self):
        day = WorkDay()
        day.clear_interval()

        time_one = Time(12, 30, Meridian.PM)
        time_two = Time(2, 30, Meridian.PM)

        date_one = Date(4, 29, 2021)
        date_two = Date(4, 29, 2021)

        date_time_one = DateTime(date_one, time_one)
        date_time_two = DateTime(date_two, time_two)

        day.set_interval_start(date_time_one)
        day.end_current_interval(date_time_two)

        time_one = Time(2, 30, Meridian.PM)
        date_time_one = DateTime(date_one, time_one)
        day.set_interval_start(date_time_one)

        self.assertEqual(day.check_for_incomplete_interval(), True)


if __name__ == '__main__':
    unittest.main()
