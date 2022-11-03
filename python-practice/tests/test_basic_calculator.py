import unittest
from unittest.mock import patch
from basic_calculator import BasicCalculator

class BasicCalculatorTest(unittest.TestCase):
    
    def setUp(self):
        self.bc_obj = BasicCalculator()

    def test_calculation(self):
        """Testing with integers."""
        self.input_mocking("romulo", "3 4 5")
        result_message_1 = self.bc_obj.print_results()
        expected_message_1 = "Your name is: romulo\nThe numbers you inputed are: 3.00, 4.00 and, 5.00\nThe result is: 35.00"
        self.assertEqual(expected_message_1, result_message_1)

        """Testing with floats."""
        self.input_mocking("romulo", "3.2 4.5 5.8")
        result_message_2 = self.bc_obj.print_results()
        expected_message_2 = "Your name is: romulo\nThe numbers you inputed are: 3.20, 4.50 and, 5.80\nThe result is: 44.66"
        self.assertEqual(expected_message_2, result_message_2)

        """Testing with negative integers."""
        self.input_mocking("romulo", "-3 -4 -5")
        result_message_3 = self.bc_obj.print_results()
        expected_message_3 = "Your name is: romulo\nThe numbers you inputed are: -3.00, -4.00 and, -5.00\nThe result is: 35.00"
        self.assertEqual(expected_message_3, result_message_3)

        """Testing with negative floats"""
        self.input_mocking("romulo", "-3.2 -4.5 -5.8")
        result_message_4 = self.bc_obj.print_results()
        expected_message_4 = "Your name is: romulo\nThe numbers you inputed are: -3.20, -4.50 and, -5.80\nThe result is: 44.66"
        self.assertEqual(expected_message_4, result_message_4)

    def test_name(self):
        """Testing all caps."""
        self.input_mocking("ROMULO", "3 4 5")
        result_message_1 = self.bc_obj.print_results()
        expected_message_1 = "Your name is: ROMULO\nThe numbers you inputed are: 3.00, 4.00 and, 5.00\nThe result is: 35.00"
        self.assertEqual(expected_message_1, result_message_1)

        """Testing random caps."""
        self.input_mocking("rOmULo", "3 4 5")
        result_message_2 = self.bc_obj.print_results()
        expected_message_2 = "Your name is: rOmULo\nThe numbers you inputed are: 3.00, 4.00 and, 5.00\nThe result is: 35.00"
        self.assertEqual(expected_message_2, result_message_2)


    def input_mocking(self, inp1: str, inp2: str):
        """Using a context manager patch method is useful in the sense that there are more than
        one input inside each test, creating a method for it makes the inputing reusable and readable."""
        with patch("builtins.input", return_value=inp1):
            self.bc_obj.user_input_name()
        with patch("builtins.input", return_value=inp2):
            self.bc_obj.user_input_values()