import unittest
import multiple

class multiple_test(unittest.TestCase):
    
    def test_zero_division(self):
        assert multiple.is_multiple(20, 0) == None

    def test_is_divisor(self):
        assert multiple.is_multiple(6,2) == True
        assert multiple.is_multiple(6,3) == True
        assert multiple.is_multiple(6,6) == True

    def test_not_divisor(self):
        assert multiple.is_multiple(9,4) == False
        assert multiple.is_multiple(9,5) == False 
        assert multiple.is_multiple(9,7) == False
    