"""
    Create Mine Sweeper game layout with  5 rows and 5 columns

    * Add menus to you Mine Sweeper game to be able to
    - Start new game
    - Change game layout (5x5, 5x8, 8x8)
    - Close game
"""
import tkinter
from random import randint
from tkinter import messagebox


class MineSweeper():
    title = "Minesweeper"
    game_layout = {'5x5': [5, 5], '5x8': [5, 8], '8x8': [8, 8]}

    def __init__(self, option: str='5x5'):
        self.main_window = tkinter.Tk()
        self.main_window.title(self.title)
        self.add_menu()
        for row in range(self.game_layout[option][0]):
            for col in range(self.game_layout[option][1]):
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
            warning = messagebox.askyesno(title=self.title, message="Game over! Try again?")
        if warning:
            self.new_game()
        elif warning is False:
            self.main_window.destroy()

    def new_game(self):
        self.main_window.destroy()
        new_game = MineSweeper()
        new_title = 'New ' + self.title
        new_game.main_window.title(new_title)
        new_game.run()

    def layout_1(self):
        self.main_window.destroy()
        new_game = MineSweeper('5x8')
        new_title = '5x8 ' + self.title
        new_game.main_window.title(new_title)
        new_game.run()

    def layout_2(self):
        self.main_window.destroy()
        new_game = MineSweeper('8x8')
        new_title = '8x8 ' + self.title
        new_game.main_window.title(new_title)
        new_game.run()

    def add_menu(self):
        main_layer = tkinter.Menu(self.main_window)
        self.main_window.config(menu=main_layer)
        layer_1 = tkinter.Menu(self.main_window)
        main_layer.add_cascade(label='Options', menu=layer_1)
        layer_1.add_command(label='New Game', command=self.new_game)
        layer_2 = tkinter.Menu(self.main_window)
        layer_1.add_cascade(label='Change layout', menu=layer_2)
        layer_2.add_command(label='5x5', command=self.new_game)
        layer_2.add_command(label='5x8', command=self.layout_1)
        layer_2.add_command(label='8x8', command=self.layout_2)
        layer_1.add_separator()
        layer_1.add_command(label='Close', command=self.main_window.destroy)


    def run(self):
        self.main_window.mainloop()


login = MineSweeper()
login.run()