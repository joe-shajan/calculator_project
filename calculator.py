from tkinter import *
window = Tk()
window.geometry("500x500")


def changetext():
    a.config(text='button clicked')


button1 = Button(window, text="ok", width=5, height=1, bg="yellow", command=changetext)
button2 = Button(window, text="ok", width=5, height=1, bg="yellow", command=changetext)
button3 = Button(window, text="ok", width=5, height=1, bg="yellow", command=changetext)
button4 = Button(window, text="ok", width=5, height=1, bg="yellow", command=changetext)
button5 = Button(window, text="ok", width=5, height=1, bg="yellow", command=changetext)

a = Label(window, text="welcome")

button1.grid(row=0, column=0)
button2.grid(row=0, column=1)
button3.grid(row=0, column=2)
button4.grid(row=0, column=3)
button5.grid(row=1, column=0)


window.mainloop()
