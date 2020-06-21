#연습문제1
from tkinter import *
top = Tk()
top.title("체크버튼")
cnvs=Canvas(top,width=500,height=180,bg='white')
cnvs.grid(row=0,column=0)

def r():
    cnvs.delete(ALL)
    if a1.get()==1:
        cnvs.create_rectangle(10,10,490,170)
    if a2.get()==1:
        cnvs.create_oval(10,10,490,170)
    if a3.get()==1:
        cnvs.create_line(10,10,490,170)
a1=IntVar()
a2=IntVar()
a3=IntVar()
fr = Frame(top)
fr.grid()
bt1 = Checkbutton(fr,text="직사각형",command=r,variable=a1)
bt2 = Checkbutton(fr,text="타 원",command=r,variable=a2)
bt3 = Checkbutton(fr,text="직 선",command=r,variable=a3)
bt1.pack(padx=10,side='left')
bt2.pack(padx=10,side='left')
bt3.pack(padx=10,side='left')
top.mainloop()

#연습문제2
from tkinter import *
top = Tk()
top.title("Calculator")
txt = Entry(top,width=33,bg='yellow')
txt.grid(row=0,column=0,columnspan=5)
list=['7','8','9','/','C',
      '4','5','6','*','(',
      '1','2','3','-',')',
      '0','.','=','+','']
rowindex=1
colindex=0
for btext in list:
    Button(top,text=btext,width=5).grid(row=rowindex,column=colindex)
    colindex +=1
    if colindex>4:
        rowindex +=1
        colindex =0
def click(key):
    if key=="=":
        result = eval(txt.get())
        s=str(result)
        txt.insert(END,"="+s)
    elif key=="C":
        txt.delete(0,END)
    else:
        txt.insert(END,key)
rowindex=1
colindex=0
for btext in list:
    def process(t=btext):
        click(t)
    Button(top,text=btext,width=5,command=process).grid(row=rowindex,column=colindex)
    colindex+=1
    if colindex>4:
        rowindex+=1
        colindex=0
top.mainloop()

#과제
from tkinter import *
top=Tk()
top.title("라디오버튼과 체크버튼")
cnvs=Canvas(top,width=500,height=200,bg='white')
cnvs.grid(row=0,column=0)
def r():
    cnvs.delete(ALL)
    pick=int(v.get())
    check=int(ch.get())
    if check==1:
        if pick==1:
            cnvs.create_rectangle(10,10,490,190,fill='pink')
        elif pick==2:
            cnvs.create_oval(10,10,490,190,fill='pink')
        elif pick==3:
            cnvs.create_line(10,10,490,190,fill='pink')
    else:
        if pick==1:
            cnvs.create_rectangle(10,10,490,190)
        elif pick==2:
            cnvs.create_oval(10,10,490,190)
        elif pick==3:
            cnvs.create_line(10,10,490,190)
v=IntVar()
ch=IntVar()
fr=Frame(top)
fr.grid()
bt1=Radiobutton(fr,text="직사각형",value=1,variable=v,command=r)
bt2=Radiobutton(fr,text="타 원",value=2,variable=v,command=r)
bt3=Radiobutton(fr,text="직 선",value=3,variable=v,command=r)
bt4=Checkbutton(fr,text="색채우기",variable=ch)
bt1.grid(row=1,column=0)
bt2.grid(row=1,column=1)
bt3.grid(row=1,column=2)
bt4.grid(row=1,column=3)
