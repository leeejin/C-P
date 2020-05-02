import turtle
#1번
for l in range(1,6):
    for b in range(5-l):
        print(" ",end="")
    for s in range(2*l-1):
        print('*',end="")
    print()
    
#2번
t = turtle.Turtle()
for i in range(5):
    for l in range(5):
        t.forward(100)
        t.left(72)
    t.left(72)
