import unittest
import is_even


class is_even_test(unittest.TestCase):
    def test_even(self):
        assert is_even.is_even(6) == True
        assert is_even.is_even(100.0) == True
        assert is_even.is_even(-24) == True

    def test_odd(self):
        assert is_even.is_even(9) == False
        assert is_even.is_even(-1) == False
        assert is_even.is_even(5.5) == False
        assert is_even.is_even(2.1) == False
