import unittest
from unittest.mock import patch
from basic_calculator import BasicCalculator

class BasicCalculatorTest(unittest.TestCase):
    
    def setUp(self):
        self.bc_obj = BasicCalculator()

    def test_calculation(self):
        self.input_mocking("romulo", "3 4 5")
        result_message = self.bc_obj.print_results()
        self.assertEqual("Your name is: romulo\n\
The numbers you inputed are: 3.00, 4.00 and, 5.00\n\
The result is: 35.00", result_message)

    def input_mocking(self, inp1: str, inp2: str):
        """Using a context manager patch method is useful in the sense that there are more than
        one input inside each test, creating a method for it makes the inputing reusable and readable."""
        with patch("builtins.input", return_value=inp1):
            self.bc_obj.user_input_name()
        with patch("builtins.input", return_value=inp2):
            self.bc_obj.user_input_values()