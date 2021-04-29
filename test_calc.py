import unittest
import calc

class TestCase(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(calc.addition(1,2), 3)
        self.assertEqual(calc.addition(5.5,5), 10.5)
        self.assertEqual(calc.addition(-5,1), -4)

    def test_subtraction(self):
        self.assertEqual(calc.subtract(2, 1), 1)
        self.assertEqual(calc.subtract(200, 100), 100)
        self.assertEqual(calc.subtract(-20, 5), -25)
        self.assertEqual(calc.subtract("two", 1), 2)

    def test_multiply(self):
        self.assertEqual(calc.multiply(2, 1), 2)
        self.assertEqual(calc.multiply(.50, .50), .25)
        self.assertEqual(calc.multiply(100, 200), 20000)
        self.assertEqual(calc.multiply(-5, 5), -25)

    def test_devide(self):
        self.assertEqual(calc.devide(2, 1), 2)
        self.assertEqual(calc.devide(5, 2), 2.5)
        self.assertEqual(calc.devide(-10, 2), -5)


#enables running directly
if __name__ == "__main__":
    unittest.main(verbosity=2)