import random
import turtle

#1번
a = int(input('a입력:'))
b = int(input('b입력:'))
if a>b:
    print('a가 b보다',a-b,'만큼 더 크다')
elif a==b:
    print('a와 b는 같다')
else:
    print('b가 a보다',b-a,'만큼 더 크다')

#2번
user = input('가위바위보:')
com = random.randrange(3)
list = ['가위','바위','보']
if com==0:
    com = list[0]
    if user == list[2]:
        print('사용자:',user,'컴퓨터:',com,'==>컴퓨터 승')
    elif user == list[1]:
        print('사용자:',user,'컴퓨터:',com,'==>사용자 승')
    else:
        print('사용자:',user,'컴퓨터:',com,'==>비김')
elif com==1:
    com = list[1]
    if user == list[2]:
        print('사용자:',user,'컴퓨터:',com,'==>사용자 승')
    elif user == list[0]:
        print('사용자:',user,'컴퓨터:',com,'==>컴퓨터 승')
    else:
        print('사용자:',user,'컴퓨터:',com,'==>비김')
else:
    com = list[2]
    if user == list[0]:
        print('사용자:',user,'컴퓨터:',com,'==>사용자 승')
    elif user == list[1]:
        print('사용자:',user,'컴퓨터:',com,'==>컴퓨터 승')
    else:
        print('사용자:',user,'컴퓨터:',com,'==>비김')
        
#3번
t = turtle.Turtle()
t.penup()
t.goto(0,0)
t.pendown()
s1 = int(turtle.textinput('입력창','변1:'))
s2 = int(turtle.textinput('입력창','변2:'))
s3 = int(turtle.textinput('입력창','변3:'))
if s3**2 == s1**2 + s2 **2:
    t.forward(s1*10)
    t.left(90)
    t.forward(s2*10)
    t.home()
else:
    t.write('직각삼각형이 아님:')

