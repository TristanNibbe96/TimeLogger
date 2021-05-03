import unittest
from src.Time import Time
from src.Time import Meridian


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


if __name__ == '__main__':
    unittest.main()
