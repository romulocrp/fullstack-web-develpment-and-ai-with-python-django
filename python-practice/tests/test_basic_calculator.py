import unittest
from unittest.mock import patch
from basic_calculator import BasicCalculator

class BasicCalculatorTest(unittest.TestCase):
    
    def setUp(self):
        self.bc_obj = BasicCalculator()

    def tearDown(self):
        pass



    """@patch("builtins.input", lambda _: "y")"""
    def test_calculation(self):
        self.bc_obj.name = "romulo"
        self.bc_obj.a = 3
        self.bc_obj.b = 4
        self.bc_obj.c = 5
        result_message = self.bc_obj.print_results()
        self.assertEqual("Your name is: romulo\n\
The numbers you inputed are: 3.00, 4.00 and, 5.00\n\
The result is: 35.00", result_message)
