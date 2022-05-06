from tkinter import *

window = Tk()

mainmenu = Menu(window)
window.config(menu = mainmenu)

filemenu = Menu(mainmenu)
mainmenu.add_cascade(labe = 'file', menu = filemenu)

filemenu.add_command(label = 'open')
filemenu.add_separator()
filemenu.add_command(label = 'exit')

window.mainloop()
