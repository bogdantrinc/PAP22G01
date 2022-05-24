import tkinter

main_window = tkinter.Tk()
main_window.title("Login form")
label1 = tkinter.Label(main_window, text='Login')
label1.grid(row=0, column=1)
label2 = tkinter.Label(main_window, text='Username:')
label2.grid(row=1, column=0)
entry_1 = tkinter.Entry(main_window)
entry_1.grid(row=1, column=1)
label5 = tkinter.Label(main_window, text='Password:')
label5.grid(row=2, column=0)
entry_2 = tkinter.Entry(main_window)
entry_2.grid(row=2, column=1)

main_window.mainloop()