import unittest
from examen_1 import GiveMeMoreTime

login = GiveMeMoreTime()

class TestMyApp(unittest.TestCase):

    def test_get_text(self):
        self.assertEqual('Europe/Tallinn', login.get_text())

    def test_get_text_new(self):
        login.time_zone_list.clear()
        self.assertEqual(None, login.get_text())

if __name__ == "__main__":
    unittest.main()
