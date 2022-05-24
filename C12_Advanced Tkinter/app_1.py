import tkinter


class MineSweeper():
    title = "Minesweeper"

    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title(self.title)
        self.add_menu()

        for i in range(3):
            for j in range(3):
                self.__setattr__(f'label{i, j}',
                                 tkinter.Label(self.main_window, text=self.is_bomb(), width=10, height=2))
                self.__setattr__(f'button{i, j}', tkinter.Button(self.main_window, text='o',width=10,height=3, command=self.do_nothing))
                self.__getattribute__(f'label{i, j}').grid(row=i, column=j)
                self.__getattribute__(f'button{i, j}').grid(row=i, column=j)

    def add_menu(self):
        main_l1 = tkinter.Menu(self.main_window)
        self.main_window.config(menu=main_l1)

        main_l2 = tkinter.Menu(self.main_window)
        main_l1.add_cascade(label='Games', menu=main_l2)

        main_l3 = tkinter.Menu(self.main_window)
        main_l2.add_cascade(label='New game', menu=main_l3)

        main_l3.add_command(label='Game_1', command=self.new_window)
        main_l3.add_command(label='Game_2', command=quit)

        main_l2.add_separator()

        main_l2.add_command(label='Exit', command=quit)

    def new_window(self):
        new_window = MineSweeper()
        new_title = self.title + ' Clone'
        new_window.main_window.title(new_title)
        new_window.run()

    def is_bomb(self):
        return 1

    def do_nothing(self):
        pass

    def run(self):
        self.main_window.mainloop()


login = MineSweeper()
login.run()