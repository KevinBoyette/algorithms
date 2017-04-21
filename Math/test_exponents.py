from exponents import recur_exp_by_squaring
from exponents import iterative_squaring_exponent_method
from exponents import isEven
from exponents import isOdd
from exponents import isNegative
from exponents import isZero
from exponents import isOne


def setup_module(module):
    print ("setup_module      module:%s" % module.__name__)


def teardown_module(module):
    print ("teardown_module   module:%s" % module.__name__)


def setup_function(function):
    print ("setup_function    function:%s" % function.__name__)


def teardown_function(function):
    print ("teardown_function function:%s" % function.__name__)


def test_isEven():
    print("Is 100 Even? ")
    assert isEven(100) == True
    print("Is 101 Even? ")
    assert isEven(101) == False


def test_isOdd():
    print("Is 100 Odd? ")
    assert isOdd(100) == False
    print("Is 101 Even? ")
    assert isOdd(101) == True


def test_isNegative():
    print("Is 1230 negative? ")
    assert isNegative(1230) == False
    print("Is -1230 negative? ")
    assert isNegative(1230) == False


def test_isZero():
    print("Is 100 == 0? ")
    assert isZero(100) == False
    print("Is 0 == 0? ")
    assert isZero(0) == True


def test_isOne():
    print("Is 1 == 1? ")
    assert isOne(1) == True
    print("Is 101 == 1? ")
    assert isOne(101) == False


class TestRecurExpBySquaring:

    def test_recur_exp_by_squaring_2_3(self):
        print("Testing Exponention by squaring - 2 ** 3")
        assert recur_exp_by_squaring(2, 3) == 8

    def test_recur_exp_by_squaring_3_3(self):
        print("Testing Exponention by squaring - 3 ** 3")
        assert recur_exp_by_squaring(3, 3) == 27

    def test_recur_exp_by_squaring_16_8(self):
        print("Testing Exponention by squaring - 16 ** 8")
        assert recur_exp_by_squaring(16, 8) == 4294967296

    def test_recur_exp_by_squaring_123_0(self):
        print("Testing Exponention by squaring - 123 ** 0")
        assert recur_exp_by_squaring(123, 0) == 1

    def test_recur_exp_by_squaring_17_1(self):
        print("Testing Exponention by squaring - 17 ** 1")
        assert recur_exp_by_squaring(17, 1) == 17

    def test_recur_exp_by_squaring_10_neg1(self):
        print("Testing Exponention by squaring - 10 ** -1")
        assert recur_exp_by_squaring(10, -1) == 0.1

    def test_recur_exp_by_squaring_point1_neg2(self):
        print("Testing Exponention by squaring - 0.1 ** -2")
        assert recur_exp_by_squaring(0.1, -2) == 100


class TestIterativeExpBySquaringMethod:

    def test_iterative_squaring_exponent_method_2_3(self):
        print("Testing Exponention by squaring - 2 ** 3")
        assert iterative_squaring_exponent_method(2, 3) == 8

    def test_iterative_squaring_exponent_method_3_3(self):
        print("Testing Exponention by squaring - 3 ** 3")
        assert iterative_squaring_exponent_method(3, 3) == 27

    def test_iterative_squaring_exponent_method_16_8(self):
        print("Testing Exponention by squaring - 16 ** 8")
        assert iterative_squaring_exponent_method(16, 8) == 4294967296

    def test_iterative_squaring_exponent_method_123_0(self):
        print("Testing Exponention by squaring - 123 ** 0")
        assert iterative_squaring_exponent_method(123, 0) == 1

    def test_iterative_squaring_exponent_method_17_1(self):
        print("Testing Exponention by squaring - 17 ** 1")
        assert iterative_squaring_exponent_method(17, 1) == 17

    def test_iterative_squaring_exponent_method_10_neg1(self):
        print("Testing Exponention by squaring - 10 ** -1")
        assert iterative_squaring_exponent_method(10, -1) == 0.1

    def test_iterative_squaring_exponent_method_point1_neg2(self):
        print("Testing Exponention by squaring - 0.1 ** -2")
        assert iterative_squaring_exponent_method(0.1, -2) == 100
