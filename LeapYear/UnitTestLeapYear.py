import unittest
import Leapyear

class TestLeapYear(unittest.TestCase):
    def test_is_leap_year(self):
        self.assertTrue(Leapyear.Leapyear(2000))
        self.assertTrue(Leapyear.Leapyear(2400))




if __name__ == '__main__':
    unittest.main(verbosity= 2)