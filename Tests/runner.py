# tests/runner.py
import unittest

from Math import test_exponents
from Sorts import test_sorts

# Test Suite Init
loader = unittest.TestLoader()
suite = unittest.TestSuite()

# Load Tests
suite.addTests(loader.loadTestsFromModule(test_exponents))
suite.addTests(loader.loadTestsFromModule(test_sorts))

# Initialize Runner
runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)
print(result)
