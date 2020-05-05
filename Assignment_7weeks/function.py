#함수 정의 및 호출
def sum(begin,end):
    result =0
    for i in range(begin,end+1):
        result = result+i
    return result
print('1~10까지의 합:',sum(1,10))

#함수작성
def func(arg):
     n = arg +100
     return n

print('함수결과',func(7))

#정의 되지 않은 함수 호출 //main()함수를 마지막에 call하는 것은 가능
def main():
    print(power(10,2))
def power(x,y):
    result =1
    for i in range(y):
        result = result * x
    return result
main()

#ex
def getGrade(n):
    if n>= 90:
        return 'A'
    elif n>=80:
        return 'B'
    elif n>=70:
        return 'C'
    elif n>=60:
        return 'D'
    else:
        return 'F'
while 1:
    n = eval(input('점수: '))
    if n<0 or n>100:
        print('  종료함')
        break;
    print(getGrade(n)+'학점')

#함수 정의 및 예제
import turtle
t = turtle.Turtle()
def square(length):
    for i in range(4):
        t.forward(length)
        t.left(90)
leng = 50
for n in range(3):
    square(leng)
    leng=leng+30
