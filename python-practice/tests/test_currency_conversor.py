import unittest
from unittest.mock import patch
from currency_conversor import CurrencyConverter

class CurrencyConversorTest(unittest.TestCase):

    def setUp(self):
        self.cc_obj = CurrencyConverter()

    def input_mocking(self, inp1: str, inp2: str):
        """Using a context manager patch method is useful in the sense that there are more than
        one input inside each test, creating a method for it makes the inputing reusable and readable."""
        with patch("builtins.input", return_value=inp1):
            self.cc_obj.amount_input()
        with patch("builtins.input", return_value=inp2):
            self.cc_obj.currency_input()