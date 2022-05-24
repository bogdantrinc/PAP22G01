import tkinter

def print_something():
    print("Message")

main_window = tkinter.Tk()
main_window.title("My app")

button1 = tkinter.Button(main_window, text="Sign in", command=print_something)
button1.grid(row=0, column=1)

# text = tkinter.Text(main_window)
# text.grid(row=0, column=1)

entry = tkinter.Entry(main_window)
entry.grid(row=0, column=0)

main_window.mainloop()