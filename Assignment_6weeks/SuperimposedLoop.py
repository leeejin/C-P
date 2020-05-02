import turtle
import random
t = turtle.Turtle()
for k in range(10):
    degree = random.randint(1,360)
    length = random.randint(10,100)
    t.left(degree)
    t.forward(length)

#중첩루프
for x in range(3):
    print('x=',x)
    for y in range(3):
        print('\t','y=',y)
        
#2중 FOR문 별 쌓기
N = int(input('수 입력:'))
star = '*'
for v in range(N):
    tstar =''
    for x in range(N):
        tstar = tstar + star
    print(tstar)

#패턴 반복 예제
for i in range(5):
    for j in range(i+1):
        print('*',end = '')
    print()

#피타고라스 삼각형
count =0
for a in range(1,51,1):
    for b in range(a,51,1):
        for c in range(b,51,1):
            if((a**2+b**2)==c**2):
                print(a,b,c)
                count=count+1
print("피타고라스 수: %d 개"%count)

#반복문의 else
for n in range(1,10):
    for x in range(1,n):
        if n%2==0:
            break
        print(x,end = ' ')
    else:
        print('*')
        
for n in range(2,100):
    for x in range(2,n):
        if n %x ==0:
            break
    else:
        print(n,end = ' ')
