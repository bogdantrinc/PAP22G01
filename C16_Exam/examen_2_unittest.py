import tkinter
import unittest
from examen_2 import ScreenSaver

login = ScreenSaver()

class TestMyApp(unittest.TestCase):

    def test_change_color(self):
        self.assertEqual(True, login.change_color())

    def test_change_color_new(self):
        self.assertEqual('Changed!', login.button_change(event=tkinter.Event))

if __name__ == "__main__":
    unittest.main()
