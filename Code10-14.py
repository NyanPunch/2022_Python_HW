from tkinter import *
from tkinter import messagebox

def imageclick(event) :
    messagebox.showinfo('mouse', 'mouse clicked on image')

window = Tk()
window.geometry('400x400')

photo = PhotoImage(file = 'cat2.gif')
label1 = Label(window, image= photo)

label1.bind("<Button>", imageclick)

label1.pack(padx = 10, pady = 10,expand=1,anchor = CENTER)

window.mainloop()
