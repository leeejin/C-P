#모듈 import 및 메인 윈도우 설정
from tkinter import *
top=Tk()
top.title("BMI 계산")

def calc():
    height = float(en1.get())
    weight = float(en2.get())
    bmi = weight / height **2
    lb4["text"] = str(bmi)

lb1 = Label(top,text="키(m)")
lb2 = Label(top,text="BMI")
lb3 = Label(top,text="몸무게(Kg)")
lb4 = Label(top)
lb1.grid(row=0, column=0)
lb2.grid(row=0, column=2)
lb3.grid(row=1, column=0)
lb4.grid(row=1, column=2)

en1= Entry(top)
en2=Entry(top)
en1.grid(row=0, column=1)
en2.grid(row=1, column=1)

bt1=Button(top, width=10, text="계 산",command=calc)
bt1.grid(row=2, column=2)

top.mainloop()

#tkinter 위젯
#단순 위젯: Button(버튼을 표시하기 위해 사용),
#Canavs(화면에 직선,타원,다각형 등과 같은 모양을 그리기 위해 사용),
#Checkbutton(체크박스처럼 여러가지 값을 표시하기 위해 사용.한 번에 여러개 선택가능),
#Entry(한 줄의 텍스트 값을 입력받는 필드를 표시하기 위해 사용),
#Label(다른 위젯을 위한 한줄 제목을 제공하기 위해 사용,이미지 가능),
#Message(여러 줄의 텍스트 필드를 표시하기 위해 사용) 등
#컨테이너 위젯: 다른위젯을 안에 포함할 수 있는 위젯으로서
#Frame(다른 위젯들을 구성하기 위한 컨테이너 위젯으로 사용),
#Toplevel(분리된 윈도우 컨테이너를 제공하기 위해 사용),
#LabelFrame(복합 윈도우 레이아웃을 위한 컨테이너 위젯),
#PanedWindow(수직,수평으로 배열된 여러 위젯들을 포함하는 컨테이너 위젯) 등
#Radiobutton(여러 가지 값을 표시하기 위해 사용. 한 번에 한 개만 선택 가능)
#Scale(슬라이더 위젯을 제공하기 위해 사용)
#Scrollbar(Listbox와 같은 위젯에 스크롤 기능을 주기 위해 사용)
#Text(여러 줄에 텍스트를 표시하기 위해 사용)
#Toplevel(분리된 윈도우 컨테이너를 제공하기 위해 사용)
#Spinbox(고저오딘 수의 값들로부터 선택할 수 있는 표준 Entry위젯의 변형)
#Listbox : 사용자가 선택 가능한 여러 개의 리스트를 제공하기 위해 사용)
#Menu(다양한 명령을 제공하기 위해 사용.
#Menubutton(메뉴들을 표시하기 위해 사용) 내에 포함됨)


#Label 위젯
#w = Label(master, option=value, ...)
#텍스트나 이미지를 표현하기 위해 사용하는 상자형태의 도구
#텍스트나 이미지는 필요시 수정가능
#첫번째 매개변수 : 부모 윈도우(여기서는 master)내에 레이블 배치
#두번째 매개변수 : 다양한 옵션 : 키-값 쌍으로 표현

#하나의 레이블(Label)이 있는 윈도우를 생성
from tkinter import *
window = Tk()
label = Label(window,text="Hello GUI world!",width=20,height=2,
              font='helvetica 14 italic',
              relief=RAISED)
label.pack()
window.mainloop()
#이것도 똑같음 !
from tkinter import *
window=Tk()
lb=Label(window)
lb['text']="Hello GUI world!"
lb['width']=20
lb['height']=2
lb['font']='helvetica 14 italic'
lb['relief']=RAISED
lb.pack()
window.mainloop()
#anchor 위젯의 공간이 넓을때, 텍스트의 위치, default는 CENTER
#relief 레이블의 테두리 형태. FLAT(default),GROOVE,RAISED 등
#justify 여러 줄의 텍스트 배치시 문단 정렬방법, default 는 CENTER
#padx,pady 위젯내의 텍스트의 좌우,상하 추가 공간, default는 1
#레이블에 이미지 표시 : image옵션
from tkinter import *
top=Tk()
logo = PhotoImage(file="pyimage1.png")
lbImg= Label(top,image=logo).pack()
top.mainloop()

from tkinter import *
top= Tk()
logo = PhotoImage(file="pyimage1.png")
lbl=Label(top,image=logo).pack(side='left')
txt = '''A GUI is a type of user
interface that allows users
to interact with devices
in a graphical way.'''
lb2=Label(top,padx=10,
          justify=LEFT,
          text=txt).pack(side='right')
top.mainloop()
#하나의 레이블에 이미지와 텍스트 겹쳐서 출력 : compound 옵션 사
from tkinter import *
top= Tk()
logo = PhotoImage(file="pyimage1.png")
txt = '''A GUI is a type of user
interface that allows users
to interact with devices
in a graphical way.'''
lb= Label(top,padx=10,
          compound=CENTER,
          text=txt,
          image=logo).pack(side='right')
top.mainloop()

#Button 위젯
#w=Button(master,option=value)
#버튼옵션
#command : 버튼이 클릭될 때 호출되는 함수나 메소드
#text : 위젯에 표시하기 위한 텍스트
#image : 위젯에 표시하기 위한 이미지

#하나의 버튼(Button)이 있는 윈도우를 생성

from tkinter import *
top=Tk()
bt = Button(top,text="클릭하세요!")
bt.pack()
top.mainloop()

#compound 옵션: 이미지와 텍스트 동시 설정
from tkinter import *
top=Tk()
click=PhotoImage(file='pyimage1.png')
bt =Button(top,image=click,text="클릭하세요!",compound=LEFT).pack()
top.mainloop()
#없으면, 이미지만 설정 가능

#버튼의 주요기능 : 클릭 시, 어떠한 동작을 수행하도록 하는것
#command옵션 사용: callback함수
from tkinter import *
top=Tk()
def ft():
    print("클릭했습니다.")
bt=Button(top,text="클릭하세요!",command=ft).pack()
top.mainloop()

#Entry위젯
#w=Entry(parent,option ...)
from tkinter import *
top=Tk()
top.title("엔트리")
ent=Entry(top).pack()
mainloop()
#레이블과 엔트리가 표시된 예
from tkinter import *
top=Tk()
lb=Label(top,text="User Name").pack(side=LEFT)
en=Entry(top).pack(side=RIGHT)
top.mainloop()
#옵션 show='*' 사용시 입력내용 숨김
#데이터 입출력위한 메소드
#delete(fst,lst): 위젯의 fst위치부터 lst위치 앞까지의 문자열 지움. lst없으면 fst위치의 한문자만 지움
#get() : 현재 엔트리내의 텍스트를 문자열로 반환
#insert(index,s) : index위치의 문자 앞에 문자열 s 삽입

#get()활용
from tkinter import *
top = Tk()
def showName():
    print("User Name:",en.get())
lb=Label(top,text = "User Name").grid(row=0)
en = Entry(top)
en.grid(row=0, column=1)
bt1= Button(top,text='Show',command=showName)
bt2= Button(top, text='Quit',command=top.quit)
bt1.grid(row=1,column=0)
bt2.grid(row=1,column=1)
top.mainloop()

#텍스트(Text)위젯 : 여러줄의 문자열을 입력할 경우 사용
from tkinter import *
top=Tk()
txt = Text(top,height=5,width=60)
txt.insert(END,"텍스트 위젯은 여러 줄의\n텍스트를 표시 할 수 있습니다.")
txt.pack()
top.mainloop()

#체크버튼
from tkinter import *
w= Tk()
w.title("체크버튼")
def varState():
    print('var1:',v1.get())
    print('var2:',v2.get())
    print('var3:',v3.get())
lb = Label(w, text = "선호하는 프로그래밍 언어 모두 선택:")
lb.pack(padx=10)
v1=IntVar()
v2=IntVar()
v3=IntVar()
cb1 = Checkbutton(w, text = "Python", variable=v1)
cb2 = Checkbutton(w, text = "Java", variable=v2)
cb3 = Checkbutton(w, text = "C++", variable=v3)
cb1.pack(padx=10, anchor=W)
cb2.pack(padx=10, anchor=W)
cb3.pack(padx=10, anchor=W)
bt = Button(w, text='Show', command=varState).pack()
w.mainloop()
#라디오버튼 : 체크박스와 달리 하나의 그룹안에서는 한 개의 버튼만 선택
from tkinter import *
w= Tk()
w.title("라디오버튼")
def show():
    choice = str(v.get())+'언어 선택함'
    lb2.config(text=choice)
v = StringVar()
lb1=Label(w,text="가장 선호하는 프로그래밍 언어 선택")
lb2=Label(w)
lb1.pack(padx=10)
rb1=Radiobutton(w,text="Python",variable=v, value='Python',command=show)
rb2=Radiobutton(w,text="Java",variable=v, value='Java',command=show)
rb3=Radiobutton(w,text="C++",variable=v, value='C++',command=show)
rb1.pack(padx=20,anchor=W)
rb2.pack(padx=20,anchor=W)
rb3.pack(padx=20,anchor=W)
lb2.pack()
mainloop()

#압축(pack)배치 관리자
#side 옵션: 버튼을 가로로배치
from tkinter import *
w=Tk()
b1=Button(w,text="첫번째 버튼")
b2=Button(w,text="두번째 버튼")
b1.pack(side=LEFT,padx=10)
b2.pack(side=LEFT,padx=10)
w.mainloop()
#버튼의 배치를 부모 위젯의 넓이에 맞추기위해 fill=X 옵션 사용
#패딩 옵션: 버튼의 배치를 부모 위젯의 상하좌우에 공간
from tkinter import *
w=Tk()
Button(w,text="Python 언어").pack(fill=X,padx=10,side=LEFT)
Button(w,text="C++ 언어").pack(fill=X,padx=10,pady=5,side=LEFT)
Button(w,text="Visual Basic 언어").pack(fill=X,padx=10,side=BOTTOM)
mainloop()

#버튼의 텍스트 변경
from tkinter import *
w=Tk()
b1=Button(w,text="첫번째 버튼")
b2=Button(w,text="두번째 버튼")
b1.pack(side=LEFT, padx=10)
b2.pack(side=LEFT, padx=10)
b1["text"]="one"
b2["text"]="Two"
w.mainloop()

#격자(grid)배치 관리자
from tkinter import *
window=Tk()
window.title("grid 배치 예제")
l1=Label(window,text="화씨")
l2=Label(window,text="섭씨")
l1.grid(row=0,column=0)
l2.grid(row=1,column=0)
e1=Entry(window)
e2=Entry(window)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
b1=Button(window,text="화씨->섭씨")
b2=Button(window,text="화씨->섭씨")
b1.grid(row=2, column=0)
b2.grid(row=2,column=1,sticky=W)
window.mainloop()

#rowspan과 columnspan 옵션을 사용
from tkinter import *
w=Tk()
bt0 = Button(w,text='c0',width=10,height=3)
Button(w,text='r0, c1',width=10).grid(row=0,column=1)
Button(w,text='r1, c1',width=10).grid(row=1,column=1)
Button(w,text='r2, c0',width=10).grid(row=2,column=0)
Button(w,text='r2, c1',width=10).grid(row=2,column=1)
bt0.grid(row=0, column=0,rowspan=2)
w.mainloop()

#for루프 이용, Label 위젯에 전화기 다이얼 생성
from tkinter import *
w=Tk()
lbls= [['1','2','3'],['4','5','6'],['7','8','9'],['*','0','#']]
for r in range(4):
    for c in range(3):
        lbl=Label(w,relief=RAISED,padx=10,text=lbls[r][c])
        lbl.grid(row=r,column=c)
w.mainloop()
