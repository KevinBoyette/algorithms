# tests/runner.py
import unittest

from Math import test_exponents
from Sorts import test_sorts
from StringMatching import test_knuth_morris_pratt

# Test Suite Init
loader = unittest.TestLoader()
suite = unittest.TestSuite()

# Load Tests
suite.addTests(loader.loadTestsFromModule(test_exponents))
suite.addTests(loader.loadTestsFromModule(test_sorts))
suite.addTests(loader.loadTestsFromModule(test_knuth_morris_pratt))

# Initialize Runner
runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)
print(result)
