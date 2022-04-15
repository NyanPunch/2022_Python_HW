#확대 축소 가능한 이미지
from tkinter import *
from tkinter.filedialog import *

def func_open() : #파일 오픈
    global filename #전역 변수 선언하여 확대 축소 함수 사용
    filename = askopenfilename(parent = window, filetypes = (("GIF 파일", "*.gif"), ("모든 파일", "*.*")))
    photo = PhotoImage(file = filename)
    pLabel.configure(image = photo)
    pLabel.image = photo

def func_exit() : #프로그램 종료
    window.quit()
    window.destroy()

def func_zoom(event) : #이미지 확대
    photo = PhotoImage(file = filename) #파일메뉴에서 가져온 gif 확대
    photo = photo.zoom(3, 3)
    pLabel.configure(image = photo)
    pLabel.image = photo

def func_subsample(event) : #이미지 축소
    photo = PhotoImage(file = filename) #파일메뉴에서 가져온 gif 축소
    photo = photo.subsample(3, 3) 
    pLabel.configure(image = photo)
    pLabel.image = photo

window = Tk()
window.geometry("500x500")
window.title("연습문제")

photo = PhotoImage()
pLabel = Label(window, image = photo)
#방향키 위, 아래 사용 시 확대 축소
window.bind("<Down>", func_subsample)
window.bind("<Up>", func_zoom)

pLabel.pack(expand=1, anchor = CENTER)
#파일 메뉴 부분
mainMenu = Menu(window)
window.config(menu = mainMenu)
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "파일", menu = fileMenu)
fileMenu.add_command(label = "파일 열기", command = func_open)
fileMenu.add_separator()
fileMenu.add_command(label = "프로그램 종료", command = func_exit)

window.mainloop()
