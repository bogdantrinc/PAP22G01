import json
import requests
import tkinter


class MainMenu:
    title = 'Main Menu'

    def __init__(self, main_window: tkinter.Tk):
        self.main_window = main_window
        self.main_window.title(self.title)
        self.add_menu()

    def add_menu(self):
        # main_l1 = tkinter.Menu(self.main_window)
        # self.main_window.config(menu=main_l1)
        result = requests.get(url='http://worldtimeapi.org/api/timezone/Europe')
        my_zones = json.loads(result.text)
        for i in range(len(my_zones)):
            self.__setattr__(f'button{i}',
                             tkinter.Button(self.main_window, text=my_zones.pop(), command=self.new_window))
            self.__getattribute__(f'button{i}').grid(row=i // 23, column=i % 23)

    def new_window(self):
        window = tkinter.Tk()
        new_title = self.title + 'Copy'
        window.title(new_title)
        label = tkinter.Label(window, text="abcd")
        label.pack()

    def run(self):
        self.main_window.mainloop()


if __name__ == '__main__':
    window = tkinter.Tk()
    main_menu = MainMenu(window)
    main_menu.run()
