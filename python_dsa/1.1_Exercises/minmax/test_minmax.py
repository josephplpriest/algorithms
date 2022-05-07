import unittest
import minmax


class test_minmax(unittest.TestCase):
    def test_empty(self):
        assert minmax.minmax([]) == None

    def test_single(self):
        assert minmax.minmax([1]) == (1, 1)
        assert minmax.minmax([-10]) == (-10, -10)

    def test_min(self):
        assert minmax.minmax([1, 5, 29, 30])[0] == 1
        assert minmax.minmax([-10, 5, 5.5, 30])[0] == -10
        assert minmax.minmax([0.01, 5, 29, 30])[0] == 0.01

    def test_max(self):
        assert minmax.minmax(range(0, 100))[1] == 99
        assert minmax.minmax([-5, -5, -10])[1] == -5
        assert minmax.minmax([0.01, 10.1, 100.1]) == (0.01, 100.1)
