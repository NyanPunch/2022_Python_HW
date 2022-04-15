#좋아하는 동물 투표하기
from tkinter import *

def myFunc() : #선택한 라디오 버튼으로 이미지를 바꾼다
    if var.get() == 1 :
        labelImage.configure(image = photo1)
    elif var.get() == 2 :
        labelImage.configure(image = photo2)
    else :
        labelImage.configure(image = photo3)

var, labelImage = 0, None
photo1, photo2, photo3 = [None]*3

if __name__ == '__main__' :
    window = Tk()
    window.geometry("400x400")
    window.title("애완동물 선택하기")
    labelText = Label(window, text = "좋아하는 동물 투표 ",fg = "blue", font = ("바탕체", 20))
            #2019038054 김경민
    var = IntVar()  #라디오 버튼이 활성화 중인 이미지를 화면에 보일 수 있게 한다
    rb1 = Radiobutton(window, text = "강아지", variable = var, value = 1)
    rb2 = Radiobutton(window, text = "고양이", variable = var, value = 2)
    rb3 = Radiobutton(window, text = "햄스터", variable = var, value = 3)
    buttonOk = Button(window, text = "사진보기", command = myFunc)

    photo1 = PhotoImage(file = "gif/dog7.gif")
    photo2 = PhotoImage(file = "gif/cat8.gif")
    photo3 = PhotoImage(file = "gif/hamster.gif")
    
    #사진보기 버튼을 누르기 전 초기 레이블 이미지 상태
    labelImage = Label(window, width = 200, height = 200, bg = "yellow", image = None)

    #여백을 조절하여 출력
    labelText.pack(padx = 5, pady = 5)
    rb1.pack(padx = 5, pady = 5)
    rb2.pack(padx = 5, pady = 5)
    rb3.pack(padx = 5, pady = 5)
    buttonOk.pack(padx = 5, pady = 5)
    labelImage.pack(padx = 5, pady = 5)

    window.mainloop()
