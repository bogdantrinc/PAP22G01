import unittest
from examen_final import GiveMeMoreTime

login = GiveMeMoreTime()

class TestMyApp(unittest.TestCase):

    def test_compare(self):
        location_1 = "Europe/Bucharest"
        location_2 = "Europe/Budapest"
        self.assertEqual(1, login.compare(location_1=location_1, location_2=location_2))

if __name__ == "__main__":
    unittest.main()

