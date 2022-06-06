import tkinter


class MyApp():

    @staticmethod
    def print_something():
        print('message')

    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title('MyApp')

        button1 = tkinter.Button(self.main_window, text="Sign In", command=self.print_something)
        button1.grid(row=0, column=0)
        entry = tkinter.Entry(self.main_window, takefocus=True)
        entry.grid(row=0, column=2)

    def add_text(self):
        text = tkinter.Text(self.main_window)
        text.grid(row=0, column=1)

    def run(self):
        self.main_window.mainloop()


login = MyApp()
#login.add_text()
login.run()
