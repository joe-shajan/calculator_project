from tkinter import *
win = Tk() #create window
win.geometry("312x370")#size of the window
win.resizable(0,0)#prevent from resizing window
win.title("calculator")

######functions#############
#btn click functions continuisoly updates the inpur field
def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

#bt_clear to clear the input field
def bt_clear():
    global expression
    expression = ""
    input_text.set("")

def bt_equal():
    global expression
    result = str(eval(expression))
    input_text.set(result)
    expression = " "


expression = " "
#StringVar() is used to get the instance of input field
input_text = StringVar()

#frame for input field
input_frame = Frame(win, width=312,height=50,bd=0)
input_frame.pack(side=TOP)

#creating input field inside frame
input_field = Entry(input_frame, font=("arial",18,"bold"), textvariable = input_text, width=50, bg="white", bd=0,justify=RIGHT)
input_field.grid(row=0,column=0)
input_field.pack(ipady=10)

#frame for buttons
btns_frame = Frame(win, width=312,height=272.5,bg="#fff")
btns_frame.pack()

#first row

clear = Button(btns_frame, text = "C", fg = "black", width = 24, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: bt_clear()).grid(row = 0, column = 0, columnspan = 3)
divide = Button(btns_frame, text="/", fg="black", width=6, height=3, bd=0, bg="#fff", cursor="hand2",
                command=lambda: btn_click("/")).grid(row=0, column=3)

#second row
seven = Button(btns_frame, text="7", fg="black", width=6, height=3, bd=0, bg="#fff", cursor="hand2",
               command=lambda: btn_click(7)).grid(row=1, column=0)

eight = Button(btns_frame, text="8", fg="black", width=6, height=3, bd=0, bg="#fff", cursor="hand2",
               command=lambda: btn_click(8)).grid(row=1, column=1)

nine = Button(btns_frame, text="9", fg="black", width=6, height=3, bd=0, bg="#fff", cursor="hand2",
              command=lambda: btn_click(9)).grid(row=1, column=2)

multiply = Button(btns_frame, text="*", fg="black", width=6, height=3, bd=0, bg="#fff", cursor="hand2",
                  command=lambda: btn_click("*")).grid(row=1, column=3)


#thirdrow
four = Button(btns_frame, text="4", fg="black", width=6, height=3, bd=0, bg="#fff", cursor="hand2",
               command=lambda: btn_click(4)).grid(row=2, column=0)

five = Button(btns_frame, text="5", fg="black", width=6, height=3, bd=0, bg="#fff", cursor="hand2",
               command=lambda: btn_click(5)).grid(row=2, column=1)

six = Button(btns_frame, text="6", fg="black", width=6, height=3, bd=0, bg="#fff", cursor="hand2",
              command=lambda: btn_click(6)).grid(row=2, column=2)

minus = Button(btns_frame, text="-", fg="black", width=6, height=3, bd=0, bg="#fff", cursor="hand2",
                  command=lambda: btn_click("-")).grid(row=2, column=3)

#fourth row

one = Button(btns_frame, text="1", fg="black", width=6, height=3, bd=0, bg="#fff", cursor="hand2",
               command=lambda: btn_click(1)).grid(row=3, column=0)

two = Button(btns_frame, text="2", fg="black", width=6, height=3, bd=0, bg="#fff", cursor="hand2",
               command=lambda: btn_click(2)).grid(row=3, column=1)

three = Button(btns_frame, text="3", fg="black", width=6, height=3, bd=0, bg="#fff", cursor="hand2",
              command=lambda: btn_click(3)).grid(row=3, column=2)

plus = Button(btns_frame, text="+", fg="black", width=6, height=3, bd=0, bg="#fff", cursor="hand2",
                  command=lambda: btn_click("+")).grid(row=3, column=3)

#fifth row
zero = Button(btns_frame, text="0", fg="black", width=6, height=3, bd=0, bg="#fff", cursor="hand2",
               command=lambda: btn_click(0)).grid(row=4, column=0)

point = Button(btns_frame, text=".", fg="black", width=6, height=3, bd=0, bg="#fff", cursor="hand2",
               command=lambda: btn_click(".")).grid(row=4, column=1)

equals = Button(btns_frame, text="=", fg="black", width=6, height=3, bd=0, bg="#fff", cursor="hand2",
              command=lambda: bt_equal()).grid(row=4, column=2)




win.mainloop()
