"""
#Exam Python M2

Create Python UI application that will work as a random color screensaver:
* retrieve 3 random numbers every 10 seconds: (50p)
    * https://csrng.net/csrng/csrng.php?min=0&max=255 * create app to run in full screen and apply solid color from the 3 numbers:
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
import time
import tkinter

import requests


class ScreenSaver():
    title = "ScreenSaver"

    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title(self.title)
        self.my_color = tkinter.StringVar()
        self.my_color.set('#ffffff')
        self.__setattr__(f'button', tkinter.Button(self.main_window, text='Push', width=100, height=10, textvariable=self.my_color, command=self.get_hex_code))
        self.__getattribute__(f'button').grid(row=0, column=2, sticky='nesw')

    def new_window(self):
        new_window = ScreenSaver()
        new_title = self.title + ' Clone'
        new_window.main_window.title(new_title)
        new_window.run()

    def get_hex_code(self):
        cod_hexa = ''
        for i in range(3):
            time.sleep(1)
            result = requests.get(url=f'https://csrng.net/csrng/csrng.php?min=0&max=255')
            numar_random = result.json()[0]["random"]
            cod_hexa += str(hex(numar_random)).replace('0x', '')
        return self.my_color.set(f'#{cod_hexa}')

    def run(self):
        self.main_window.attributes('-fullscreen', True)
        self.main_window.mainloop()


login = ScreenSaver()
login.run()