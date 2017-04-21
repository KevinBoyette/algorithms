# Test For The Knuth Morris Pratt Algorithm
from knuth_morris_pratt import kmp, prefix_kmp


class TestKMP:

    def test_kmp(self):
        assert kmp("hello world", "ll") == 2
        assert kmp("whomp dingo", "ding") == 6
        assert kmp("python3 > python2", ">") == 8
        assert kmp(" {'key' : 'value' }", ":") == 8

    def test_prefix_kmp(self):
        assert prefix_kmp("world") == [-1, 0, 0, 0, 0]
        assert prefix_kmp("tuna fish") == [-1, 0, 0, 0, 0, 0, 0, 0, 0]
        assert prefix_kmp(
            "?!@abcabc?!!") == [-1, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 2]
        assert prefix_kmp(
            "abcabcbacbacbabc") == [-1, 0, 0, -1, 0, 0, 3, -1, 1, 0, -1, 1, 0, -1, 0, 0]
