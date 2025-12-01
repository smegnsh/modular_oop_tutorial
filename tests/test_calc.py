# Import the unittest framework for writing test cases
import unittest
import sys
import os
# Add the scripts folder to Python path
#sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../scripts')))
# Import the functions we expect to exist in calc.py
# NOTE: These functions DO NOT exist yet → Tests will fail (RED phase)
from scripts.calc import *


# Create a class that inherits from unittest.TestCase
# This class will contain all test methods
class TestCalc(unittest.TestCase):

    # Test the add() function
    def test_add(self):
        # Check that add(2, 3) returns 5
        self.assertEqual(add(2, 3), 5)

    # Test the subtract() function
    def test_subtract(self):
        # Check subtract(5, 2) returns 3
        self.assertEqual(subtract(5, 2), 3)

    # Test multiply() function
    def test_multiply(self):
        # Check multiply(4, 3) returns 12
        self.assertEqual(multiply(4, 3), 12)

    # Test divide() function
    def test_divide(self):
        # Check divide(10, 2) returns 5
        self.assertEqual(divide(10, 2), 5)

    # Test division-by-zero should raise an exception
    def test_divide_by_zero(self):
        # Expect ZeroDivisionError when dividing by zero
        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)


# This allows running tests by executing this file directly
if __name__ == '__main__':
    unittest.main()
