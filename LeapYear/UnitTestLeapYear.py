import unittest
import Leapyear

class TestLeapYear(unittest.TestCase):
    def test_is_leap_year(self):
        self.assertTrue(Leapyear.Leapyear(2000))
        self.assertTrue(Leapyear.Leapyear(2400))

    def test_isnot_leap_year(self):
        self.assertFalse(is_leap_year(1900))
        self.assertFalse(is_leap_year(2100))




if __name__ == '__main__':
    unittest.main(verbosity= 2)