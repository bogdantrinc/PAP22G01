"""
    Create Mine Sweeper game layout with  5 rows and 5 columns
"""
import tkinter


class MineSweeper():
    title = "Minesweeper"

    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title(self.title)
        for row in range(5):
            for col in range(5):
                self.__setattr__(f'label{row, col}',
                                 tkinter.Label(self.main_window, text=self.is_bomb(), width=10, height=2))
                self.__setattr__(f'button{row, col}', tkinter.Button(self.main_window, text='O', width=10, height=5, command=self.do_nothing))
                self.__getattribute__(f'label{row, col}').grid(row=row, column=col)
                self.__getattribute__(f'button{row, col}').grid(row=row, column=col)

    def is_bomb(self):
        return 1

    def do_nothing(self):
        pass

    def run(self):
        self.main_window.mainloop()


login = MineSweeper()
login.run()