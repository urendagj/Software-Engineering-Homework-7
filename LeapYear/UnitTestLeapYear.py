import unittest
import Leapyear

class TestLeapYear(unittest.TestCase):
    def test_is_leap_year(self):
        self.assertTrue(Leapyear.Leapyear(2000))
        self.assertTrue(Leapyear.Leapyear(2012))
        self.assertTrue(Leapyear.Leapyear(2020))
        self.assertTrue(Leapyear.Leapyear(2400))

    def test_isnot_leap_year(self):
        self.assertFalse(Leapyear.Leapyear(1900))
        self.assertFalse(Leapyear.Leapyear(2007))
        self.assertFalse(Leapyear.Leapyear(1845))
        self.assertFalse(Leapyear.Leapyear(2500))




if __name__ == '__main__':
    unittest.main(verbosity= 2)
