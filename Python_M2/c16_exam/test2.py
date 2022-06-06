import json
import requests
import tkinter
import time


class MainMenu:
    title = 'Main Menu'

    def __init__(self):
        self.main_window = tkinter.Tk()
        self.my_color = tkinter.StringVar()
        self.my_color.set('#ffffff')
        self.main_window.title(self.title)
        self.add_menu()

    def make_request(self):
        cod_hexa = ''
        for i in range(3):
            time.sleep(1)
            result = requests.get(url='https://csrng.net/csrng/csrng.php?min=0&max=255')
            json_resp = result.json()[0]["random"]
            cod_hexa += str(hex(json_resp)).replace('0x', '')
        print(cod_hexa)
        return cod_hexa

    def add_menu(self):
        self.main_window.attributes('-fullscreen', True)
        label1 = tkinter.Label(self.main_window, text='Red text', bg=f'#{self.make_request()}')
        label1.bind("<Button-1>", self.change_color)
        label1.bind("<Button-3>", self.run_loop)
        label1.grid(row=0, column=0)

    def run_loop(self, event):
        while True:
            time.sleep(10)
            self.change_color('')
            label1 = tkinter.Label(self.main_window, text='Red text', bg=f'#{self.my_color.get()}')
            label1.grid(row=0, column=0)

    def change_color(self, event):
        self.my_color.set(f'{self.make_request()}')
        print(self.my_color.get())

    def run(self):
        self.main_window.mainloop()


if __name__ == '__main__':
    main_menu = MainMenu()
    main_menu.run()
