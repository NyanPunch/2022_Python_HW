from tkinter import *
from tkinter import messagebox

window = Tk()

def myFunc() :
    if chk.get() == 0 :
        messagebox.showinfo("", "checkbutton is off")
    else :
        messagebox.showinfo("","checkbutton is on")

chk = IntVar()
cb1 = Checkbutton(window, text = "클릭하세요", variable = chk, command = myFunc)

cb1.pack()

window.mainloop()
