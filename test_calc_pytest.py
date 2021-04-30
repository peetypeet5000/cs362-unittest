import pytest
import calc

class TestCalc:
    def test_addition(self):
        assert calc.addition(2, 2) == 4

    def test_subtraction(self):
        assert calc.subtract(10, 5) == 5
        assert calc.subtract(-5, 0) == -5

    def test_multiply(self):
        assert calc.multiply(5, 0) == 0
        assert calc.multiply(5, -1) == -5

    def test_devide(self):
        assert calc.devide(10, 3) == (10/3)
        assert calc.devide(5, 0) == 0

