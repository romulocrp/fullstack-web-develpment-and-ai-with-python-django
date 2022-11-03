import unittest
from datetime import date
from unittest.mock import patch
from currency_conversor import CurrencyConverter

class CurrencyConversorTest(unittest.TestCase):

    request_moment = date.today()

    def setUp(self):
        self.cc_obj = CurrencyConverter()

    def test_amounts(self):
        """Testing positive integer value."""
        self.input_mocking("200", "ars")
        result_message_1 = self.cc_obj.print_converted_amount()
        expected_message_1 = f"The converted amount is: 30165.40 ARS at\
 {CurrencyConversorTest.request_moment.month}/{CurrencyConversorTest.request_moment.day}/{CurrencyConversorTest.request_moment.year}."
        self.assertEqual(expected_message_1, result_message_1)

    def input_mocking(self, inp1: str, inp2: str):
        """Using a context manager patch method is useful in the sense that there are more than
        one input inside each test, creating a method for it makes the inputing reusable and readable."""
        with patch("builtins.input", return_value=inp1):
            self.cc_obj.amount_input()
        with patch("builtins.input", return_value=inp2):
            self.cc_obj.currency_input()