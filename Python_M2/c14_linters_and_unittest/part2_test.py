import unittest
from file1 import calculate_area


class TestAreaFunction(unittest.TestCase):

    def test_valid_area(self):
        self.assertEqual(calculate_area(2, 3), 6)

    def test_length_str(self):
        self.assertRaises(TypeError, calculate_area, '2', 3)

    def test_high_str(self):
        self.assertRegex(calculate_area(2, '3'), r'\d\d')


if __name__ == "__main__":
    unittest.main()
