"""
## Exam Python M2

Create Python UI application that will retrieve all timezones from this link http://worldtimeapi.org/api/timezone/Europe and two random number from https://csrng.net/csrng/csrng.php?min=1&max=2116:
The application must randomly select 2 time zones based on the retrieved numbers and when the "Compare" button is pushed the time difference will be displayed
UI implementation ()
Detailed description:
  - Pylint shows no errors or warnings (10p)
  - At least one unittest created for at lest one function (10p)
    - recommended for function to get/calculate random number
  - File menu has Close option which will close the application (10p)
  - UI has 2 fields with timezones, one compare button and one field for time difference (30p)
  - Time difference is correctly displayed when the "Compare" button is pressed (20p)
  - Retrieving timezones or random numbers is done in parallel (20p)

Layout
```
##################################
# Timezone1 # Timezone2 # Result #
##################################
#        Compare Button          #
##################################
```
"""
import asyncio
import json
import time
import tkinter
import aiohttp
import requests


class GiveMeMoreTime:
    """A Python UI application."""
    title = "GiveMeMoreTime"

    def __init__(self):
        """Constructor."""
        self.time_zone_list = []
        self.main_window = tkinter.Tk()
        self.main_window.title(self.title)
        self.label_1 = tkinter.Label(self.main_window, text="Timezone 1!", width=25, height=5)
        self.label_2 = tkinter.Label(self.main_window, text="Timezone 2!", width=25, height=5)
        self.label_3 = tkinter.Label(self.main_window, text="Result!", width=25, height=5)
        self.button = tkinter.Button(self.main_window, text="Compare!", bg='gray', command=self.get_numbers, height=5)
        self.label_1.grid(row=0, column=0)
        self.label_2.grid(row=0, column=1)
        self.label_3.grid(row=0, column=2)
        self.button.grid(row=1, columnspan=3, sticky='nsew')
        self.add_menu()

    def add_menu(self):
        """App menu with close button."""
        main_layer = tkinter.Menu(self.main_window)
        self.main_window.config(menu=main_layer)
        layer = tkinter.Menu(self.main_window)
        main_layer.add_cascade(label='File menu', menu=layer)
        layer.add_command(label='Close', command=quit)

    async def get_time(self):
        """Returns all timezones."""
        async with aiohttp.ClientSession() as client:
            result = await client.request(method='GET', url=f'http://worldtimeapi.org/api/timezone/Europe')
        return json.loads(await result.text())

    def get_numbers(self):
        """Returns two timezones."""
        numbers = []
        for _ in range(2):
            time.sleep(0.1)
            result = requests.get(url=f'https://csrng.net/csrng/csrng.php?min=1&max=2116')
            try:
                numbers.append(int(result.json()[0]['random']/46))
            except KeyError:
                return self.get_numbers()
        self.time_zone_list = asyncio.run(self.get_time())
        self.time_zone_list = [self.time_zone_list[numbers[0]], self.time_zone_list[numbers[1]]]
        self.label_1.config(text=self.time_zone_list[0].strip('Europe/'))
        self.label_2.config(text=self.time_zone_list[1].strip('Europe/'))
        self.label_3.config(text=f"Difference: {self.compare(self.time_zone_list[0], self.time_zone_list[1])} h")

    def compare(self, location_1, location_2):
        """Compares two timezones."""
        timezone_1 = requests.get(url=f'http://worldtimeapi.org/api/timezone/{location_1}')
        timezone_2 = requests.get(url=f'http://worldtimeapi.org/api/timezone/{location_2}')
        return abs(int(timezone_1.json()['utc_offset'][:-3]) - int(timezone_2.json()['utc_offset'][:-3]))

    def run(self):
        """Runs the program by calling the Tk main loop."""
        self.main_window.mainloop()


login = GiveMeMoreTime()
login.run()

