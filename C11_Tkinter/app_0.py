import tkinter

main_window = tkinter.Tk()
main_window.title('My app')

# Ordinea label-urilor conteaza
label1 = tkinter.Label(main_window, text='RED Text', bg='red')
label1.pack(fill=tkinter.Y)

label2 = tkinter.Label(main_window, text='GREEN Text', bg='green')
label2.pack(fill=tkinter.X)

label3 = tkinter.Label(main_window, text='BLUE Text', bg='blue')
label3.pack(side=tkinter.LEFT, fill=tkinter.Y)

label4 = tkinter.Label(main_window, text='YELLOW Text', bg='yellow')
label4.pack(side=tkinter.RIGHT, fill=tkinter.Y)

label5 = tkinter.Label(main_window, text='MAGENTA Text', bg='magenta')
label5.pack(side=tkinter.BOTTOM, fill=tkinter.X)

main_window.mainloop()