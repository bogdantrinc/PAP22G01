import tkinter


class MyApp():
    # @staticmethod
    # def print_something():
    #     print('message!')
    list_user_pass = {'Ivan': 'ivan', 'Bogdan': 'bogdan', 'Adrian': 'adrian'}
    counter = 0
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("MyApp")

        # button1 = tkinter.Button(self.main_window, text='Sign In', command=self.print_something)
        # button1.grid(row=0,column=0)
        # entry = tkinter.Entry(self.main_window, takefocus=True)
        # entry.grid(row=0,column=2)
        for count, text in enumerate(['Username: ', 'Password: ']):
            label = tkinter.Label(self.main_window, text=text)
            label.grid(row=count, column=0)

        for count, text in enumerate(['user', 'passw']):
            self.__setattr__(text, tkinter.Entry(self.main_window, show=None if text != 'passw' else '*'))
            self.__getattribute__(text).grid(row=count, column=1)

        button1 = tkinter.Button(self.main_window, text='Sign In', command=self.get_user_data)
        button1.grid(row=2, column=1)

    def add_text(self):
        text = tkinter.Text(self.main_window)
        text.grid(row=0, column=1)

    def get_user_data(self):
        try:
            assert self.list_user_pass[self.user.get()] == self.passw.get()
        except:
            self.counter += 1
        else:
            print('Login successful')

        if self.counter >= 3:
            exit(11)


    def run(self):
        self.main_window.mainloop()


login = MyApp()
# login.add_text()
login.run()