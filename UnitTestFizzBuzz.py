import unittest
import FizzBuzz

class TestCase(unittest.TestCase):
   def test_multiple_3_should_return_fizz(self):
       self.assertEqual(FizzBuzz.FizzBuzz(3), "Fizz")
       self.assertEqual(FizzBuzz.FizzBuzz(9), "Fizz")







if __name__ == '__main__':
    unittest.main(verbosity= 2)