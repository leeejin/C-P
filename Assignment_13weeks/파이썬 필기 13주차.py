#버튼 이벤트 처리
#button = Button(window,text="one",command=함수이름)
from tkinter import *
top = Tk()
def ft():
    print("클릭했습니다.")
bt = Button(top,text="클릭하세요!",command=ft)
bt.pack()
top.mainloop()

#텍스트 출력을 레이블에
from tkinter import *
top = Tk()
def ft():
    lb["text"]="클릭했습니다."
lb = Label(top)
lb.pack()
bt = Button(top,text="클릭하세요!",command=ft)
bt.pack()
top.mainloop()


#버튼 이벤트 처리:예제
from tkinter import *
top=Tk()
top.title("스톱 워치")
cnt = 0
def stopwatch():
    if running:
        global cnt
        cnt +=1
        lbl.config(text=str(cnt))
    top.after(1000,stopwatch)
def start():
    global running
    running = True
def stop():
    global running
    running = False
def reset():
    global cnt
    cnt =0
    lbl.config(text=str(cnt))
lbl = Label(top,font=("Helvetica",20),fg="red")
lbl.pack()
running = False
stopwatch()
b1 = Button(top,text='Start',width=25,command=start).pack()
b2 = Button(top,text='Stop',width=25,command=stop).pack()
b3 = Button(top,text='Reset',width=25,command=reset).pack()
top.mainloop()

#라디오 버튼 이벤트 처리:예제
#from tkinter import *
#top=Tk()
#top.title("라디오버튼")
#ch = IntVar()
#def choice():
#    s = ch.get()
#    if s==1:
#        img = PhotoImage(file="dog.gif")
#    elif s==2:
#        img = PhotoImage(file="cat.gif")
#    elif s==3:
#        img = PhotoImage(file="rabbit.gif")
#    elif s==4:
#        img = PhotoImage(file="bird.gif")
#    lb2=label(fr,image =img)
#    lb2.image = img
#    lb2.grid(row=0,column=1,rowspan=10)
#lb1 = Label(top,text="가장 선호하는 동물을 고르시오.").pack()
#fr = Frame(top).pack(side=LEFT)
#b1=Radiobutton(top,text="개",variable=ch,value=1,command=choice).grid(row=0,column=0)
#b2=Radiobutton(top,text="고양이",variable=ch,value=2,command=choice).grid(row=1,column=0)
#b3=Radiobutton(top,text="토끼",variable=ch,value=3,command=choice).grid(row=2,column=0)
#b4=Radiobutton(top,text="새",variable=ch,value=4,command=choice).grid(row=3,column=0)
#top.mainloop()

#엔트리위젯과 이벤트:예제
from tkinter import *
top=Tk()
top.title("BMI 계산")
def calc():
    h=float(en1.get())
    w=float(en2.get())
    bmi=w/h**2
    en1.delete(0,END)
    en2.delete(0,END)
    en3.insert(0,bmi)
lb1=Label(top,text="키(m)")
lb2=Label(top,text="BMI")
lb3=Label(top,text="몸무게(kg)")
lb1.grid(row=0,column=0)
lb2.grid(row=0,column=2)
lb3.grid(row=1,column=0)
en1=Entry(top)
en2=Entry(top)
en3=Entry(top)
en1.grid(row=0,column=1)
en2.grid(row=1,column=1)
en3.grid(row=1,column=2)
bt1=Button(top,width=10,text="계 산",command=calc)
bt1.grid(row=2,column=2)
top.mainloop()

#엔트리 위젯의 메소드
#get() : 엔트리내의 문자열을 반환
#insert(index,text) : 엔트리의 주어진 위치로 텍스트 입력
#delete(from,to) : 엔트리로부터 위치 from에서 to까지의 문자열 삭제

#색상:부분의 위젯은 배경(bg)과 전경(fg)변수를 사용하여 위젯 및 텍스트 색상을 지정
from tkinter import *
w = Tk()
bt = Button(w,text="버튼을 클릭하세요",fg="yellow",bg="green").pack()

#예제프로그램
from tkinter import *
top = Tk()
def change1():
    F = float(en1.get())
    C = (F-32)*(5/9)
    en2.insert(0,str(C))
def change2():
    C = float(en2.get())
    F = (9/5)*C+32
    en1.insert(0,str(F))
hwa = Label(top,text="화씨").grid(row=0,column=0)
sub = Label(top,text="섭씨").grid(row=0,column=1)
en1=Entry(top)
en2=Entry(top)
en1.grid(row=1,column=0)
en2.grid(row=1,column=1)
bt1 = Button(top,text="화씨->섭씨",command=change1)
bt2 = Button(top,text="섭씨->화씨",command=change2)
bt1.grid(row=0,column=2)
bt2.grid(row=1,column=2)

#연습문제
from tkinter import *
import random
top= Tk()
top.title("가위 바위 보 게임")
def r():
    global com
    com = random.randint(0,2)
    if user == sci:
        if com==0: #묵
            result = Label(top,text="사용자 패!",font="helvetica 14 italic",fg="blue").grid(row=2,column=1)
        elif com==1: #가위
            result = Label(top,text="무승부!",font="helvetica 14 italic",fg="blue").grid(row=2,column=1)
        elif com==2: #보
            result = Label(top,text="사용자 승!",font="helvetica 14 italic",fg="blue").grid(row=2,column=1)          
    elif user == roc:
        if com==0: #묵
            result = Label(top,text="무승부!",font="helvetica 14 italic",fg="blue").grid(row=2,column=1)
        elif com==1: #가위
            result = Label(top,text="사용자 승!",font="helvetica 14 italic",fg="blue").grid(row=2,column=1)
        elif com==2: #보
            result = Label(top,text="사용자 패!",font="helvetica 14 italic",fg="blue").grid(row=2,column=1)
    elif user == pap:
        if com==0: #묵
            result = Label(top,text="사용자 승!",font="helvetica 14 italic",fg="blue").grid(row=2,column=1)
        elif com==1: #가위
            result = Label(top,text="사용자 패!",font="helvetica 14 italic",fg="blue").grid(row=2,column=1)
        elif com==2: #보
            result = Label(top,text="무승부!",font="helvetica 14 italic",fg="blue").grid(row=2,column=1)

t=Label(top,text=">>>>>",font="helvetica 20 italic").grid(row=0,column=1)
user = Label(top,text="사용자").grid(row=1,column=0)
com = Label(top,text="컴퓨터").grid(row=1,column=2)
sci = Button(top,text="가위",bg="yellow",command=r,width=10).grid(row=3,column=0)
roc = Button(top,text="바위",bg="yellow",command=r,width=10).grid(row=3,column=1)
pap = Button(top,text="보",bg="yellow",command=r,width=10).grid(row=3,column=2)
top.mainloop()

#이벤트 처리
#widget.bind(event,handler)

#마우스 이벤트 처리
from tkinter import *
top = Tk()
top.title("이벤트 처리")
def mleft(event):
    print(event.x,event.y,'에서 마우스 클릭')
def mright(event):
    print('Right Button, 끝내기')
    import sys; sys.exit()
fr = Frame(top,width=240,height=100)
fr.bind("<Button-1>",mleft)
fr.bind("<Button-3>",mright)
fr.pack()
top.mainloop()

#이벤트 지정자

#<Button-1> : 마우스 버튼1이 Button위젯위에서 클릭될 때
#<B1-Motion> : 마우스 버튼1이 눌려진 채로 움직일 때
#<ButtonRelease-1> : 마우스 버튼1에서 손을 뗄 때
#<Double-Button-1> : 마우스 버튼1이 더블 클릭 될 때
#<Enter> : 마우스 포인터가 위젯으로 진입하였을 때
#<Leave> : 마우스 포인터가 위젯을 떠났을 때
#<FocusIn> : 키보드 포커스가 현재의 위젯으로 이동
#<FocusOut> : 키보드 포커스가 다른 위젯으로 이동
#<Return> : 사용자가 엔터키 입력
#<Key> : 사용자가 어떤 키라도 누를 때
#a      : 사용자가 a를 입력하였을 때
#<Shift-Up> : 시프트 키를 누른 상태로 위쪽 화살표 키 누를 때
#<Configure> : 위젯의 크기를 변경하였을 때

#마우스 이벤트 처리
from tkinter import *
top=Tk()
def sleft(event):
    print("단일 클릭, 왼쪽 버튼")
def dleft(event):
    print("더블 클릭, 왼쪽 버튼")
bt = Button(None,text = "마우스 클릭")
bt.pack()
bt.bind('<Button-1>',sleft)
bt.bind('<Double-1>',dleft)
bt.mainloop()

#키보드 이벤트 처리
from tkinter import *
top=Tk()
def key(event):
    print(event.char,"가 눌렀습니다.")
def mouse(event):
    frm.focus_set()
    print("<마우스로 프레임의 포커스 설정함>")
frm=Frame(top,width=100,height=100)
frm.pack()
frm.bind("<Key>",key)
frm.bind("<Button-1>",mouse)
top.mainloop()

#마우스 모션 이벤트 처리
from tkinter import *
top=Tk()
def motion(event):
    print("Mouse position: (",event.x,event.y,")")
    return
st= '''마우스를 움직이면 마우스의 위치를 출력한다. '''
msg = Message(top,text = st)
msg.config(bg='lightgreen',font=('times',18))
msg.pack()
msg.bind('<Motion>',motion)
top.mainloop()

#예제 프로그램
from tkinter import *
top=Tk()
def calc(event):
    lb.configure(text="결과: "+str(eval(ent.get())))
Label(top,text="파이썬 수식 입력:").pack()
ent = Entry(top)
ent.bind("<Return>",calc)
ent.pack()
lb=Label(top,text="결과:")
lb.pack()
top.mainloop()

#캔버스 위젯
from tkinter import *
top=Tk()
oldx, oldy=0,0
def begin(event):
    global oldx,oldy
    oldx,oldy = event.x,event.y
def draw(event):
    global oldx,oldy,cnvs
    newx,newy = event.x,event.y
    cnvs.create_line(oldx,oldy,newx,newy)
    oldx,oldy = newx,newy
cnvs = Canvas(top,height=100,width=150)
cnvs.pack()
cnvs.bind('<Button-1>',begin)
cnvs.bind('<Button1-Motion>',draw)
top.mainloop()

#호 그리기
from tkinter import *
top=Tk()
cnvs = Canvas(top,width=300,height=200)
cnvs.pack()
cnvs.create_arc(10,10,200,150,extent=90,style=ARC)
top.mainloop()

from tkinter import *
top=Tk()
cnvs = Canvas(top,width=300,height=200)
cnvs.pack()
cnvs.create_arc(10,10,200,150,extent=110,style=PIESLICE)
top.mainloop()

from tkinter import *
top=Tk()
cnvs = Canvas(top,width=300,height=200)
cnvs.pack()
cnvs.create_arc(10,10,200,150,extent=110,style=CHORD)
top.mainloop()

#타원 그리기
from tkinter import *
top=Tk()
cnvs = Canvas(top,width=300,height=200)
cnvs.pack()
cnvs.create_oval(10,10,200,150)
top.mainloop()

from tkinter import *
top=Tk()
cnvs = Canvas(top,width=300,height=200)
cnvs.pack()
cnvs.create_rectangle(10,10,200,150)
top.mainloop()

#다각형 그리기
from tkinter import *
top=Tk()
cnvs = Canvas(top,width=300,height=200)
cnvs.pack()
cnvs.create_polygon(10,10,150,110,250,20,fill="blue")
top.mainloop()

#텍스트 그리기
from tkinter import *
top=Tk()
cnvs = Canvas(top,width=300,height=200)
cnvs.pack()
cnvs.create_text(100,50,text='텍스트 (Text)')
cnvs.create_text(100,100,text='X')
top.mainloop()

#이미지 그리기
from tkinter import *
top=Tk()
cnvs = Canvas(top,width=300,height=200)
cnvs.pack()
img = PhotoImage(file="logo.jpg")
cnvs.create_image(100,100,anchor=NW,image=img)
cnvs.create_image(100,100,image=img)
top.mainloop()

#타원 이용한 애니메이션
from tkinter import *
from random import *
import time
top=Tk()
cnvs = Canvas(top,width=300,height=200)
cnvs.pack()
ball = cnvs.create_oval(140,90,160,110,fill="blue")
for i in range(100):
    x=randint(-10,10)
    y=randint(-10,10)
    cnvs.move(ball,x,y)
    top.update()
    time.sleep(0.1)
top.mainloop()

#캔버스 위젯과 이벤트
from tkinter import *
top=Tk()
top.title("Oval을 이용한 그림판")
pen = "blue"
def paint(event):
    x1,y1 =(event.x -1),(event.y-1)
    x2,y2 =(event.x+1),(event.y+1)
    cnvs.create_oval(x1,y1,x2,y2,outline=pen,fill=pen)
def red():
    global pen
    pen="red"
def green():
    global pen
    pen="green"
def blue():
    global pen
    pen="blue"
cnvs = Canvas(top,width=500,height=150)
cnvs.pack()
cnvs.bind("<B1-Motion>",paint)
bt1 = Button(top,text="빨간색",command=red)
bt2 = Button(top,text="초록색",command=green)
bt3 = Button(top,text="파란색",command=blue)
bt1.pack(side=LEFT,ipadx=50)
bt2.pack(side=LEFT,ipadx=50)
bt3.pack(side=LEFT,ipadx=50)
top.mainloop()
