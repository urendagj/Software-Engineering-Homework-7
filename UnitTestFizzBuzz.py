import unittest
import FizzBuzz

class TestCase(unittest.TestCase):
    def test_multiple_3_should_return_fizz(self):
        self.assertEqual(FizzBuzz.FizzBuzz(3), ['1', '2', 'fizz'])
        self.assertEqual(FizzBuzz.FizzBuzz(9), ['1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8', 'fizz'])

    def test_multiple_5_should_return_fizz(self):
        self.assertEqual(FizzBuzz.FizzBuzz(5), ['1', '2', 'fizz', '4', 'buzz'])
        self.assertEqual(FizzBuzz.FizzBuzz(20), ['1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8', 'fizz', 'buzz', '11', 'fizz', '13', '14', 'fizz', '16', '17', 'fizz', '19', 'buzz'])


    
    
  







if __name__ == '__main__':
    unittest.main(verbosity= 2)