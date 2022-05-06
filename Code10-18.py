from tkinter import *
from tkinter import messagebox

def open() :
    messagebox.showinfo('select menu', 'selected open menu')

def exit() :
    window.quit()
    window.destroy()

window = Tk()

mainmenu = Menu(window)
window.config(menu = mainmenu)

filemenu = Menu(mainmenu)
mainmenu.add_cascade(labe = 'file', menu = filemenu)

filemenu.add_command(label = 'open',command = open)
filemenu.add_separator()
filemenu.add_command(label = 'exit',command = quit)

window.mainloop()
