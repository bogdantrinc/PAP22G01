"""## Exam Python M2

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
```"""
##################################
# Timezone1 # Timezone2 # Result #
##################################
#        Compare Button          #
##################################






import json
import time
import tkinter
from tkinter import Toplevel

import requests as requests


class TimeZone():
    title = "TimeZone"
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title(self.title)
        self.add_menu()
        self.get_nr_random()
        self.butoane()
        result = requests.get(url=f'http://worldtimeapi.org/api/timezone/europe')
        self.time_zone_list = list(json.loads(result.text))
        self.t1=self.time_zone_list[1]
        self.t2 = self.time_zone_list[2]
        for i in range(2):
            for j in range(2):
                self.__setattr__(f'button{i, j}', tkinter.Button(self.main_window, text='0', width=20, height=5, command=self.main_window))
                self.__getattribute__(f'button{i, j}').grid(row=i, column=j)

    def butoane(self):

        comparare = tkinter.Button(self.main_window, command=quit, text='Comparare')
        comparare.grid(row=47, rowspan=47, column=47, sticky=tkinter.W)

        # text = tkinter.Text(self.main_window, height=30, width=30)
        # text.grid(row=3, columnspan=3)
        # T1 = tkinter.Button(self.main_window, command=quit, text='T1')
        # T1.grid(row=47, rowspan=47, column=1)
        #
        # text = tkinter.Text(self.main_window, height=30, width=30)
        # text.grid(row=3, columnspan=3)
        # T2= tkinter.Button(self.main_window, command=quit, text='T2')
        # T2.grid(row=1, rowspan=1, column=47)

        text = tkinter.Text(self.main_window, height=30, width=30)
        text.grid(row=3, columnspan=3)
    def add_menu(self):
            main_l1 = tkinter.Menu(self.main_window)
            self.main_window.config(menu=main_l1)

            main_l2 = tkinter.Menu(self.main_window)
            main_l1.add_cascade(label='File', menu=main_l2)
            main_l2.add_separator()

            main_l2.add_command(label='Close', command=quit)

    def passd(self):
        pass

    def new_window(self):
        new_window = Toplevel(self.main_window)
        new_title = self.title + ' Clone'
        new_window.title(new_title)
        result = requests.get(url=f'https://csrng.net/csrng/csrng.php?min=1&max=2116')
        label = tkinter.Label(new_window, text=result.text.replace(',','\n'))
        label.pack()
        new_window.mainloop()

    def get_text(self):
        try:
            result = self.time_zone_list.pop(0)
        except IndexError:
            result = None
        return result
    def get_nr_random(self):
        lista_nr_random = []
        for i in range(2):
            time.sleep(1)
            result = requests.get(url=f'https://csrng.net/csrng/csrng.php?min=1&max=2116')
            numar_random = result.json()[0]["random"]
            lista_nr_random.append(int(numar_random/46))
            return lista_nr_random
    def timezone(self):
        pass

    def run(self):
        self.main_window.mainloop()



login = TimeZone()
login.run()