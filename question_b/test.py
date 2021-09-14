import unittest
from compare import compare

class Test(unittest.TestCase):
    # Ensure that the first string is larger
    def test_greater(self):
        self.assertEqual(compare("1.2", "1.1"), "Greater")
        self.assertEqual(compare("1.15", "1.1"), "Greater")

    # Ensure that the first string is smaller
    def test_smaller(self):
        self.assertEqual(compare("1.1", "1.2"), "Smaller")
        self.assertEqual(compare("1.1", "1.15"), "Smaller")
    
    # Ensure that two the strings are equal
    def test_smaller(self):
        self.assertEqual(compare("1.1", "1.1"), "Equal")

if __name__ == '__main__':
    unittest.main()