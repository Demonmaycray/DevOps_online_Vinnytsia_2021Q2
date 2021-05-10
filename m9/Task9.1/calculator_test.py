import unittest
from calculator import Calculator

class CalculatorTest(unittest.TestCase):

	def test_add(self):
		number_a=5
		number_b=10
		expectet_result=15
		result = Calculator.add(self, number_a, number_b)
		self.assertEqual(result, expectet_result)

	def test_subtract(self):
		number_a=5
		number_b=10
		expectet_result=-5
		result = Calculator.subtract(self, number_a, number_b)
		self.assertEqual(result, expectet_result)
    
	def test_multiply(self):
		number_a=5
		number_b=10
		expectet_result=50
		result = Calculator.multiply(self, number_a, number_b)
		self.assertEqual(result, expectet_result)

	def test_divide(self):
		number_a=20
		number_b=10
		expectet_result=2
		result = Calculator.divide(self, number_a, number_b)
		self.assertEqual(result, expectet_result)

if __name__ == '__main__':
	unittest.main()