# # Test For The Knuth Morris Pratt Algorithm
# import unittest
# from .knuth_morris_pratt import kmp, prefix_kmp


# class TestKMP(unittest.TestCase):
#     def test_kmp(self):
#         self.assertEqual(kmp("hello world", "ll"), 2)
#         self.assertEqual(kmp("whomp dingo", "ding"), 6)
#         self.assertEqual(kmp("python3 > python2", ">"), 8)
#         self.assertEqual(kmp(" {'key' : 'value' }", ":"), 8)

#     def test_prefix_kmp(self):
#         self.assertEqual(prefix_kmp("world"), [-1, 0, 0, 0, 0])
#         self.assertEqual(prefix_kmp("tuna fish"), [-1, 0, 0, 0, 0, 0, 0, 0, 0])
#         self.assertEqual(
#             prefix_kmp("?!@abcabc?!!"), [-1, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 2])
#         self.assertEqual(
#             prefix_kmp("abcabcbacbacbabc"),
#             [-1, 0, 0, -1, 0, 0, 3, -1, 1, 0, -1, 1, 0, -1, 0, 0])


# def suite():
#     test_suite = unittest.TestSuite()
#     test_suite.addTest(unittest.makeSuite(TestKMP))
#     return test_suite


# runner = unittest.TextTestRunner()
# runner.run(suite())
