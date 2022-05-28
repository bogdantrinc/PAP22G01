import unittest
from examen_1 import GiveMeMoreTime


class TestMyApp(unittest.TestCase):

    def test_new_window(self):
        self.assertIsInstance()

    def test_get_text(self):
        self.assertRaises(IndexError, GiveMeMoreTime.get_text)


if __name__ == "__main__":
    unittest.main()
