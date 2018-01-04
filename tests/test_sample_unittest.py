import unittest
import sample_unittest

class TestSample(unittest.TestCase):
    def test_add(self):
        actual = sample_unittest.add(1,2)
        expected = 3
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
