"""
Examen python
"""
import asyncio
import json
import tkinter
from time import sleep
import aiohttp
import requests


class TimeZoneCompare:
    """
    Clasa de baza
    """
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("Compare Time Zone")
        self.add_menu()
        self.time_zone_list1 = []
        self.time_zone_list2 = []

    def add_menu(self):
        main_l1 = tkinter.Menu(self.main_window)
        self.main_window.config(menu=main_l1)
        main_l2 = tkinter.Menu(self.main_window)
        main_l1.add_cascade(label='File', menu=main_l2)
        main_l2.add_command(label='Close', command=self.main_window.destroy)

        l_timezone1 = tkinter.Label(self.main_window, text="Timezone1")
        l_timezone1.grid(row=0, column=0)

        l_timezone2 = tkinter.Label(self.main_window, text="Timezone2")
        l_timezone2.grid(row=0, column=1)

        l_result = tkinter.Label(self.main_window, text='Result')
        l_result.grid(row=0, column=2)

        b_compare = tkinter.Button(self.main_window, command=self.compare_timezones,
                                   text='Compare Button')
        b_compare.grid(row=1, column=1)

    def get_number_1(self):
        result = requests.get(url='https://csrng.net/csrng/csrng.php?min=1&max=2116')
        random_number = result.json()[0]["random"]
        return random_number % 46

    def get_number_2(self):
        result = requests.get(url='https://csrng.net/csrng/csrng.php?min=1&max=2116')
        random_number = result.json()[0]["random"]
        return random_number % 46

    async def get_timezone1(self):
        async with aiohttp.ClientSession() as client:
            result = await client.request(method='GET',
                                          url='http://worldtimeapi.org/api/timezone/europe')
        return json.loads(await result.text())

    async def get_timezone2(self):
        async with aiohttp.ClientSession() as client:
            result = await client.request(method='GET',
                                          url='http://worldtimeapi.org/api/timezone/europe')
        return json.loads(await result.text())

    def compare_timezones(self):
        self.time_zone_list1 = asyncio.run(self.get_timezone1())
        print(self.time_zone_list1[self.get_number_1()])
        sleep(2)
        self.time_zone_list2 = asyncio.run(self.get_timezone1())
        print(self.time_zone_list2[self.get_number_2()])

    def run(self):
        self.main_window.mainloop()


exam = TimeZoneCompare()
exam.run()

