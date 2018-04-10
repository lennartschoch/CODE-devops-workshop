from unittest import TestCase
from calculator.logic import Calculator


class CalculatorTests(TestCase):
    def test_mul(self):
        assert Calculator().mul(100, 10) == 1000

    def test_div(self):
        pass
