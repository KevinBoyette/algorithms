import unittest
from .exponents import recur_exp_by_squaring
from .exponents import iterative_squaring_exponent_method
from .exponents import isEven
from .exponents import isOdd
from .exponents import isNegative
from .exponents import isZero
from .exponents import isOne


class TestHelpers(unittest.TestCase):
    def test_isEven(self):
        self.assertTrue(isEven(100))
        self.assertFalse(isEven(101))

    def test_isOdd(self):
        self.assertFalse(isOdd(100))
        self.assertTrue(isOdd(101))

    def test_isNegative(self):
        self.assertFalse(isNegative(1230))
        self.assertFalse(isNegative(1230))

    def test_isZero(self):
        self.assertFalse(isZero(100))
        self.assertTrue(isZero(0))

    def test_isOne(self):
        self.assertTrue(isOne(1))
        self.assertFalse(isOne(101))


class TestRecursiveExponents(unittest.TestCase):
    def setUp(self):
        pass

    def test_recur_exp_by_squaring_2_3(self):
        print("Testing Exponention by squaring - 2 ** 3")
        self.assertEqual(recur_exp_by_squaring(2, 3), 8)

    def test_recur_exp_by_squaring_3_3(self):
        print("Testing Exponention by squaring - 3 ** 3")
        self.assertEqual(recur_exp_by_squaring(3, 3), 27)

    def test_recur_exp_by_squaring_16_8(self):
        print("Testing Exponention by squaring - 16 ** 8")
        self.assertEqual(recur_exp_by_squaring(16, 8), 4294967296)

    def test_recur_exp_by_squaring_123_0(self):
        print("Testing Exponention by squaring - 123 ** 0")
        self.assertEqual(recur_exp_by_squaring(123, 0), 1)

    def test_recur_exp_by_squaring_17_1(self):
        print("Testing Exponention by squaring - 17 ** 1")
        self.assertEqual(recur_exp_by_squaring(17, 1), 17)

    def test_recur_exp_by_squaring_10_neg1(self):
        print("Testing Exponention by squaring - 10 ** -1")
        self.assertEqual(recur_exp_by_squaring(10, -1), 0.1)

    def test_recur_exp_by_squaring_point1_neg2(self):
        print("Testing Exponention by squaring - 0.1 ** -2")
        self.assertEqual(recur_exp_by_squaring(0.1, -2), 100)


class TestIterativeExponents(unittest.TestCase):
    def setUp(self):
        pass

    def test_iterative_squaring_exponent_method_2_3(self):
        print("Testing Exponention by squaring - 2 ** 3")
        self.assertEqual(iterative_squaring_exponent_method(2, 3), 8)

    def test_iterative_squaring_exponent_method_3_3(self):
        print("Testing Exponention by squaring - 3 ** 3")
        self.assertEqual(iterative_squaring_exponent_method(3, 3), 27)

    def test_iterative_squaring_exponent_method_16_8(self):
        print("Testing Exponention by squaring - 16 ** 8")
        self.assertEqual(iterative_squaring_exponent_method(16, 8), 4294967296)

    def test_iterative_squaring_exponent_method_123_0(self):
        print("Testing Exponention by squaring - 123 ** 0")
        self.assertEqual(iterative_squaring_exponent_method(123, 0), 1)

    def test_iterative_squaring_exponent_method_17_1(self):
        print("Testing Exponention by squaring - 17 ** 1")
        self.assertEqual(iterative_squaring_exponent_method(17, 1), 17)

    def test_iterative_squaring_exponent_method_10_neg1(self):
        print("Testing Exponention by squaring - 10 ** -1")
        self.assertEqual(iterative_squaring_exponent_method(10, -1), 0.1)

    def test_iterative_squaring_exponent_method_point1_neg2(self):
        print("Testing Exponention by squaring - 0.1 ** -2")
        self.assertEqual(iterative_squaring_exponent_method(0.1, -2), 100)


def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestHelpers))
    test_suite.addTest(unittest.makeSuite(TestRecursiveExponents))
    test_suite.addTest(unittest.makeSuite(TestIterativeExponents))
    return test_suite


runner = unittest.TextTestRunner()
runner.run(suite())
