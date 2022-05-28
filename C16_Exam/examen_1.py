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
import asyncio
import json
import tkinter
from math import sqrt
from tkinter import Toplevel

import aiohttp
import requests as requests


class GiveMeMoreTime:
    """A gui application that tells you informations about different timezones."""
    title = "GiveMeMoreTime"

    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title(self.title)
        # result = requests.get(url=f'http://worldtimeapi.org/api/timezone/europe')
        # self.time_zone_list = list(json.loads(result.text))
        self.time_zone_list = asyncio.run(self.get_time())
        size = int(sqrt(len(self.time_zone_list)))
        for i in range(size):
            for j in range(size):
                place = self.get_text()
                self.__setattr__(f'button{i, j}', tkinter.Button(self.main_window, text=place, width=20, height=5, command=lambda location=place: self.new_window(location)))
                self.__getattribute__(f'button{i, j}').grid(row=i, column=j)

    def new_window(self, location: str):
        """Opens a new window containing information about the selected time zone."""
        new_window = Toplevel(self.main_window)
        new_title = self.title + f': {location}'
        new_window.title(new_title)
        result = requests.get(url=f'http://worldtimeapi.org/api/timezone/{location}')
        label = tkinter.Label(new_window, text=result.text.replace(',', '\n'))
        label.pack()
        new_window.mainloop()

    def get_text(self):
        """Pops out the time zones from the retrieved list and returns them one by one."""
        try:
            result = self.time_zone_list.pop(0)
        except IndexError:
            result = None
        return result

    async def get_time(self):
        async with aiohttp.ClientSession() as client:
            result = await client.request(method='GET', url=f'http://worldtimeapi.org/api/timezone/europe')
        return json.loads(await result.text())

    def run(self):
        """Runs the program by calling the Tk main loop."""
        self.main_window.mainloop()


login = GiveMeMoreTime()
login.run()
