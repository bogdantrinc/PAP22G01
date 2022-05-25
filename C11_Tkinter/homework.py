"""
    Create Mine Sweeper game layout with  5 rows and 5 columns
"""
import tkinter
from random import randint


class MineSweeper():
    title = "Minesweeper"

    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title(self.title)
        for row in range(5):
            for col in range(5):
                self.__setattr__(f'label{row, col}',
                                 tkinter.Label(self.main_window, text=self.is_bomb(), width=10, height=5))
                self.__setattr__(f'button{row, col}', tkinter.Button(self.main_window, text='O', width=10, height=5, command=self.push))
                self.__getattribute__(f'label{row, col}').grid(row=row, column=col)
                self.__getattribute__(f'button{row, col}').grid(row=row, column=col)

    def is_bomb(self):
        return randint(0, 1)

    def push(self):
        for row in range(5):
            for col in range(5):
                if self.__getattribute__(f'label{row, col}').cget("text") == 1:
                    print(self.__getattribute__(f'label{row, col}').cget("text"))

    def run(self):
        self.main_window.mainloop()


login = MineSweeper()
login.run()