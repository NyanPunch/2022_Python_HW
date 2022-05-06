from tkinter import *
from tkinter import messagebox

def leftclick(event) :
    messagebox.showinfo('mouse', 'left mouse clicked')

window = Tk()

window.bind("<Button-1>", leftclick)

window.mainloop()
