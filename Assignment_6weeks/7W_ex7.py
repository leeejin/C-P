import turtle
t= turtle.Turtle()
while 1:
    n = turtle.textinput('입력창','입력')
    if n=='l':
        t.left(90)
        t.forward(100)
    elif n=='r':
        t.right(90)
        t.forward(100)
    elif n=='q':
        break
