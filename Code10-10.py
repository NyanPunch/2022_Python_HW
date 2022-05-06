from tkinter import *
window = Tk()

btlist = [None]*3

for i in range(0,3) :
    btlist[i] = Button(window,text = 'Button' + str(i+1))

for bt in btlist :
    bt.pack(side=RIGHT)

window.mainloop()
