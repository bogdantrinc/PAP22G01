"""
    Create Mine Sweeper game layout with  5 rows and 5 columns

    * Add menus to you Mine Sweeper game to be able to
    - Start new game
    - Change game layout (5x5, 5x8, 8x8
    - Close game
"""
import tkinter
from random import randint
from tkinter import messagebox


class MineSweeper():
    title = "Minesweeper"

    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title(self.title)
        for row in range(5):
            for col in range(5):
                self.__setattr__(f'label{row, col}',
                                 tkinter.Label(self.main_window, text=self.is_bomb(), width=10, height=5, bg='#C8C8C8'))
                self.__setattr__(f'button{row, col}', tkinter.Button(self.main_window, width=10, height=5, command=lambda location=[row, col]: self.push(location)))
                self.__getattribute__(f'label{row, col}').grid(row=row, column=col)
                self.__getattribute__(f'button{row, col}').grid(row=row, column=col)

    def is_bomb(self):
        return randint(0, 1)

    def push(self, location: list):
        warning = None
        self.__getattribute__(f'button{location[0], location[1]}').destroy()
        if self.__getattribute__(f'label{location[0], location[1]}').cget("text") == 1:
            print("Bomba!")
            warning = messagebox.askyesno(title=self.title, message="Game over! Try again?")
        if warning:
            self.main_window.destroy()
            self.new_game()

    def new_game(self):
        new_game = MineSweeper()
        new_title = 'New ' + self.title
        new_game.main_window.title(new_title)
        new_game.run()

    def run(self):
        self.main_window.mainloop()


login = MineSweeper()
login.run()