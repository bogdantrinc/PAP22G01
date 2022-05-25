import random
import smtplib
import tkinter
from tkinter.messagebox import showwarning
from email.message import EmailMessage

class MainMenu():
    title = 'Main Menu'
    search_string = ''
    __utilizator = ''
    __parola = ''
    def __init__(self, main_window: tkinter.Tk):
        self.main_window = main_window
        self.main_window.title(self.title)
        self.add_menu()

    def add_menu(self):
        main_l1 = tkinter.Menu(self.main_window)
        self.main_window.config(menu=main_l1)
        main_l2 = tkinter.Menu(self.main_window)
        main_l1.add_cascade(label='File', menu=main_l2)
        main_l3 = tkinter.Menu(self.main_window)
        main_l2.add_cascade(label='New', menu=main_l3)
        main_l3.add_command(label='New Mail', command=self.new_mail)
        main_l3.add_command(label='New Mail in same Window', command=quit)
        main_l2.add_separator()
        main_l2.add_command(label='Close', command=quit)

    def new_mail(self):
        window = tkinter.Tk()
        new_window = MainMenu(window)
        new_title = self.title + ' Copy'
        new_window.main_window.title(new_title)

        l1 = tkinter.Label(self.main_window, text='To:')
        l1.grid(row=0, column=0, sticky=tkinter.E)
        l1 = tkinter.Label(self.main_window, text='From:')
        l1.grid(row=1, column=0, sticky=tkinter.E)
        l1 = tkinter.Label(self.main_window, text='Subject: ')
        l1.grid(row=2, column=0, sticky=tkinter.E)

        self.to_ = tkinter.Entry(self.main_window)
        self.to_.grid(row=0, column=1, sticky=tkinter.W)
        self.from_ = tkinter.Entry(self.main_window)
        self.from_.grid(row=1, column=1, sticky=tkinter.W)
        self.subject_ = tkinter.Entry(self.main_window)
        self.subject_.grid(row=2, column=1, sticky=tkinter.W)

        send = tkinter.Button(self.main_window, command=self.send_mail, text='Send')
        send.grid(row=0, rowspan=3, column=2, sticky=tkinter.W)

        self.text = tkinter.Text(self.main_window, height=30, width=90)
        self.text.grid(row=3, columnspan=3)

        search = tkinter.Label(self.main_window, text='Search: ')
        search.grid(row=4, column=0, sticky=tkinter.E)
        self.search = tkinter.Entry(self.main_window)
        self.search.bind('<KeyRelease>', self.search_text)
        self.search.grid(row=4, column=1, sticky=tkinter.W)

        self.main_window.quit()
        new_window.run()

    def run(self):
        self.main_window.mainloop()

    def get_text(self):
        print(self.text.get('0.0', tkinter.END))

    def search_text(self, v: tkinter.Event):
        # self.search_string += v.char
        result = self.text.search(self.search.get(), '0.0', tkinter.END)
        try:
            row, col = result.split('.')
        except ValueError:
            print(showwarning(title='Warning!', message='Fatal error!'))
            self.search.delete(0, tkinter.END)
        self.text.tag_add('selection', result, f'{row}.{int(col) + len(self.search.get())}')
        self.text.tag_config('selection', background='yellow')
        print(result)

    def send_mail(self):
        msg = EmailMessage()
        msg.set_content(self.text.get('0.0', tkinter.END))
        print(msg)
        msg['Subject'] = self.subject_.get()
        msg['From'] = self.from_.get()
        msg['To'] = self.to_.get()
        print(msg)
        s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        s.login(user=self.__utilizator, password=self.__parola)
        s.send_message(msg)
        s.quit()

    def login(self):
        pass


window = tkinter.Tk()
main_menu = MainMenu(window)
main_menu.run()
