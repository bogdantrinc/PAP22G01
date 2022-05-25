"""Exam Python M2

Create Python UI application that will:
    * retrieve timezones from this link: (50p)
    * http://worldtimeapi.org/api/timezone
    * Allow the user to select a timezone and open a new window indicating the time in the selected timezone using this link: (50p)
    * http://worldtimeapi.org/api/timezone/<area>/<zone>
Detailed description:
  - all windows must have title (5p)
  - all modules classes and methods must be documented (10p)
  - type hints should be used whenever possible (5p)
  - at least two unittests created for at lest one function (20p)
  - all timezones are displayed. (30p)
  - each timezone clicked will open a new window and show time in that timezone (20p)
  - retrieving time to display is done async or in separate thread or process (10p)

Note: You can choose to pack new Frame or open new window for each displayed time.
For new window you can use tkinter.TopLevel(main_window)
"""
import json
import tkinter
from tkinter import Toplevel

import requests as requests


class GiveMeMoreTime():
    title = "GiveMeMoreTime"

    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title(self.title)
        result = requests.get(url=f'http://worldtimeapi.org/api/timezone/europe')
        self.time_zone_list = list(json.loads(result.text))
        for i in range(7):
            for j in range(7):
                self.__setattr__(f'button{i, j}', tkinter.Button(self.main_window, text=self.get_text(), width=20, height=5, command=self.new_window))
                self.__getattribute__(f'button{i, j}').grid(row=i, column=j)

    def new_window(self):
        new_window = Toplevel(self.main_window)
        new_title = self.title + ' Clone'
        new_window.title(new_title)
        result = requests.get(url=f'http://worldtimeapi.org/api/timezone/europe/bucharest')
        label = tkinter.Label(new_window, text=result.text.replace(',','\n'))
        label.pack()
        new_window.mainloop()

    def get_text(self):
        try:
            result = self.time_zone_list.pop(0)
        except IndexError:
            result = None
        return result

    def run(self):
        self.main_window.mainloop()


login = GiveMeMoreTime()
login.run()