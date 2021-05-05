import unittest
from src.Time import Time
from src.Time import Meridian
from src.TimeSpan import TimeSpan


class TestTimeSubtraction(unittest.TestCase):

    def test_less_minutes_in_start_than_end(self):
        time_one = Time(12, 40, Meridian.PM)
        time_two = Time(5, 30, Meridian.PM)

        difference = time_two - time_one

        self.assertEqual(str(difference), "4:10")

    def test_more_minutes_in_start_than_end(self):
        time_one = Time(12, 40, Meridian.PM)
        time_two = Time(5, 50, Meridian.PM)

        difference = time_two - time_one

        self.assertEqual(str(difference), "5:10")

    def test_start_time_before_noon(self):
        time_one = Time(11, 40, Meridian.AM)
        time_two = Time(5, 50, Meridian.PM)

        difference = time_two - time_one

        self.assertEqual(str(difference), "6:10")

    def test_equal_minutes(self):
        time_one = Time(11, 40, Meridian.AM)
        time_two = Time(5, 40, Meridian.PM)

        difference = time_two - time_one

        self.assertEqual(str(difference), "6:00")

    def test_equal_hours(self):
        time_one = Time(5, 20, Meridian.PM)
        time_two = Time(5, 40, Meridian.PM)

        difference = time_two - time_one

        self.assertEqual(str(difference), "0:20")

    def test_equal_time(self):
        time_one = Time(5, 40, Meridian.PM)
        time_two = Time(5, 40, Meridian.PM)

        difference = time_two - time_one

        self.assertEqual(str(difference), "0:00")


class TestTimeSpanAddition(unittest.TestCase):
    def test_basic_addition(self):
        time_one = TimeSpan(1, 20)
        time_two = TimeSpan(1, 20)

        sum = time_one + time_two
        self.assertEqual(str(sum), "2:40")


if __name__ == '__main__':
    unittest.main()
