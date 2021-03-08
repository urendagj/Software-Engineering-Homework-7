import unittest
import FizzBuzz

class TestCase(unittest.TestCase):
    def test_multiple_3_should_return_fizz(self):
        self.assertEqual(FizzBuzz.FizzBuzz(3), ['1', '2', 'fizz'])
        self.assertEqual(FizzBuzz.FizzBuzz(9), ['1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8', 'fizz'])

    def test_multiple_5_should_return_fizz(self):
        self.assertEqual(FizzBuzz.FizzBuzz(5), ['1', '2', 'fizz', '4', 'buzz'])
        self.assertEqual(FizzBuzz.FizzBuzz(10), ['1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8', 'fizz', 'buzz'])

    def test_multiple_3and5_should_return_Fizzbuzz(self):
        #this test will also check to see that all 100 numbers can be output
        self.assertEqual(FizzBuzz.FizzBuzz(15), ['1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8', 'fizz', 'buzz', '11', 'fizz', '13', '14', 'fizzbuzz'])


    
    
  







if __name__ == '__main__':
    unittest.main(verbosity= 2)