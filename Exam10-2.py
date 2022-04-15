#그림판 만들기
#2019038054 김경민
from tkinter import *
from tkinter.colorchooser import *
from tkinter.simpledialog import *

def mouseclick(event) : #마우스 좌클릭 함수
    global x1,x2,y1,y2
    x1 = event.x
    y1 = event.y

def mousedrop(event) : #마우스 드롭 시 함수
    global x1,x2,y1,y2,penwidth, pencolor
    x2 = event.x
    y2 = event.y
    canvas.create_line(x1, y1, x2, y2, width = penwidth, fill = pencolor)

def getcolor() : #색상 설정
    global pencolor
    color = askcolor()
    pencolor = color[1]

def getwidth() : #선 두께 설정
    global penwidth
    penwidth = askinteger('선 두께', '선 두께(1~10)를 입력하세요', minvalue = 1, maxvalue = 10)

window, canvas = None, None
x1, x2, y1, y2 = None, None, None, None
#기본 색상 두께 지정
pencolor = 'black'
penwidth = 5

if __name__ == '__main__' :
    window = Tk()
    window.title('그림판 프로그램')
    canvas = Canvas(window, height = 300, width = 300)
    canvas.bind("<Button-1>", mouseclick) #마우스좌클릭시 실행
    canvas.bind("<ButtonRelease-1>", mousedrop) #마우스드롭시 실행
    canvas.pack()
    
    #메뉴를 만들어 선 색상과 선 두께를 고를 수 있게 한다
    mainMenu = Menu(window)
    window.config(menu = mainMenu)
    fileMenu = Menu(mainMenu)
    mainMenu.add_cascade(label = "설정", menu =fileMenu)
    fileMenu.add_command(label = '선 색상 선택', command = getcolor)
    fileMenu.add_separator() #분리선
    fileMenu.add_command(label = '선 두께 설정', command = getwidth)

    window.mainloop()
