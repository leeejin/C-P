import turtle
#1번
t= turtle.Turtle()
t.shape('turtle')
def cCircle(r):
    t.penup()
    t.goto(0,-r)
    t.pendown()
    t.circle(r)
    t.penup()
    t.home()
    t.pendown()
    return r
print(cCircle(100))
print(cCircle(70))
print(cCircle(40))

#2번
def number2(x):
    y=""
    while x>0:
        y=str(x%2)+y
        x//=2
    print(y)
def number10(bi_num):
    d = 0
    bnum = str(bi_num)
    for i, digit in enumerate(bnum):
        d += int(digit) * pow(2,len(bnum)-1-i)
    print(d)

number2(int(input('10진수 :')))
number10(int(input('2진수 :')))
