import unittest
from lines_overlap import overlap

class Test(unittest.TestCase):
    # Ensure that the lines don't overlap
    def test_does_not_overlap(self):
        self.assertFalse(overlap(0, 2, 4, 5))
        self.assertFalse(overlap(4, 5, 0, 2))

    # Ensure that the lines overlap
    def test_overlap(self):
        self.assertTrue(overlap(1, 5, 0, 3))
        self.assertTrue(overlap(0, 3, 1, 5))
        self.assertTrue(overlap(0, 5, 1, 3))
        self.assertTrue(overlap(1, 3, 0, 5))

if __name__ == '__main__':
    unittest.main()