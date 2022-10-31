import unittest
from unittest.mock import patch
from basic_calculator import BasicCalculator

class BasicCalculatorTest(unittest.TestCase):
    
    """@classmethod
    def setUpClass(cls):
        bc_obj = BasicCalculator()
        return bc_obj

    @classmethod
    def tearDownClass(cls) -> None:
        return super().tearDownClass()



    @patch("builtins.input", lambda _: "y")"""
    def test_calculation(self):
        bc_obj = BasicCalculator()
        bc_obj.name = "romulo"
        bc_obj.a = 3
        bc_obj.b = 4
        bc_obj.c = 5
        result_message = bc_obj.print_results()
        self.assertEqual("Your name is: romulo\n\
The numbers you inputed are: 3.00, 4.00 and, 5.00\n\
The result is: 35.00", result_message)
