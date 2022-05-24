import tkinter


class MineSweeper():

    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("Minesweeper")

        for i in range(3):
            for j in range(3):
                self.__setattr__(f'label{i, j}',
                                 tkinter.Label(self.main_window, text=self.is_bomb(), width=3, height=2))
                self.__setattr__(f'button{i, j}', tkinter.Button(self.main_window, text='o', command=self.do_nothing))
                self.__getattribute__(f'label{i, j}').grid(row=i, column=j)
                self.__getattribute__(f'button{i, j}').grid(row=i, column=j)

    def is_bomb(self):
        return 1

    def do_nothing(self):
        pass

    """
    0 1 0
    1 x 1
    0 1 0
    """

    def run(self):
        self.main_window.mainloop()


login = MineSweeper()
login.run()
