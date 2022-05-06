from tkinter import *

btnlist = [None]*9
fnamelist = ['cat.gif', 'cat2.gif','cat.gif', 'cat2.gif','cat.gif', 'cat2.gif','cat.gif', 'cat2.gif','cat.gif']
photolist = [None]*9
i,k=0,0
xPos,yPos=0,0
num=0

window=Tk()
window.geometry('210x210')

for i in range(0, 9) :
    photolist[i] = PhotoImage(file = ""+fnamelist[i])
    btnlist[i] = Button(window, image = photolist[i])

for i in range(0,3) :
    for k in range(0,3) :
        btnlist[num].place(x=xPos,y=yPos)
        num+=1
        xPos+=70
    xPos=0
    yPos+=70

window.mainloop()
