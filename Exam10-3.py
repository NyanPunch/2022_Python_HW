#탭 화면 만들기
from tkinter import*
from tkinter import ttk
#2019038054 김경민
window = Tk()
window.iconbitmap('python_18894.ico')

#윈도창에 탭 설정
baseTab = ttk.Notebook(window)
#개 탭 생성
Dog = ttk.Frame(baseTab)
baseTab.add(Dog, text='개')
#고양이 탭 생성
Cat = ttk.Frame(baseTab)
baseTab.add(Cat, text='고양이')
#탭 표시
baseTab.pack(expand = 1, fill = "both")
#개 이미지 업로드
photoDog = PhotoImage(file = 'gif/dog10.gif')
labelDog = Label(Dog, image = photoDog)
labelDog.pack()
#고양이 이미지 업로
photoCat = PhotoImage(file = 'gif/cat4.gif')
labelCat = Label(Cat, image = photoCat)
labelCat.pack()

window.mainloop()
