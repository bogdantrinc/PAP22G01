"""Exam Python M2

Create Python UI application that will work as a random color screensaver:
* retrieve 3 random numbers every 10 seconds: (50p)
    * https://csrng.net/csrng/csrng.php?min=0&max=255
    * create app to run in full screen and apply solid color from the 3 numbers:
    * R = hex of first number
    * G = hex of second number
    * B = hex of third number
* on click the color will refresh automatically
Detailed description:
  - all colors must be retried in parallel (5p)
  - all modules classes and methods must be documented (10p)
  - type hints should be used whenever possible (5p)
  - at least two unittests created for at lest one function (20p)
  - colored window can run full in full screen. (20p)
  - clicking the colored surface automatically updates color (10p)
  - colors are changed every 10 seconds with retrieved random color (30p)

Note: color can be set like #000000 where 00 is 0 and ff is 255
                            #RRGGBB
"""
import _tkinter
import time
import tkinter
import requests


class ScreenSaver:
    """ScreenSaver app."""
    title = "ScreenSaver"

    def __init__(self):
        """App constructor."""
        self.main_window = tkinter.Tk()
        self.main_window.title(self.title)
        self.my_color = tkinter.StringVar()
        self.my_color.set('#ffffff')
        self.label = tkinter.Label(self.main_window, textvariable=self.my_color, bg=self.my_color.get(), width=self.main_window.winfo_screenwidth(), height=self.main_window.winfo_screenheight())
        self.label.bind("<Button-1>", self.button_change)
        self.label.pack()

    def change_color(self):
        """Changes the color in hex code."""
        cod_hexa = ''
        for i in range(3):
            time.sleep(0.1)
            result = requests.get(url=f'https://csrng.net/csrng/csrng.php?min=0&max=255')
            try:
                numar_random = result.json()[0]["random"]
            except KeyError:
                return self.change_color()
            cod_hexa += str(hex(numar_random)).replace('0x', '')
        self.my_color.set(f'#{cod_hexa}')
        try:
            self.label.config(bg=self.my_color.get())
        except _tkinter.TclError:
            return self.change_color()
        return True

    def button_change(self, event: tkinter.Event):
        """Changes the color on click."""
        self.change_color()
        return 'Changed!'

    def color_loop(self):
        """Changes the color every 10 seconds."""
        while True:
            self.change_color()
            time.sleep(10)

    def run(self):
        """Runs the program by calling the Tk main loop."""
        self.main_window.attributes('-fullscreen', True)
        self.main_window.mainloop()


login = ScreenSaver()
login.run()
