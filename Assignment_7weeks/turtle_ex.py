import turtle
t = turtle.Turtle()
length =50
#한 변의 길이가 length인 n-각형
def polygon(n,legnth):
    for i in range(n):
        t.forward(length)
        t.left(360 // n)
for i  in range(10):
    polygon(5,100)
    t.left(360 / 10)
    
#참조에 의한 호출(call by reference)
print('1')
def callByRef(mylist):
    mylist += [ 1,2,3,4]
    print('Inside Func:',mylist)
    return
mylist =[10,20,30]
print('Before Call:',mylist)
callByRef(mylist)
print('After Call:',mylist)
print('2')
def callByRef(mylist):
    mylist[0] = 90
    print('Inside Func:',mylist)
    return
mylist = [10,20,30]
print('Before call:',mylist)
callByRef(mylist)
print('After Call:',mylist)

#값에 의한 호출(call by value)
def callByVal(mylist):
    mylist = [1,2,3,4]
    print('Inside Func:',mylist)
    return
mylist=[10,20,30]
print('Before Call:',mylist)
callByVal(mylist)
print('After Call:',mylist)

def modify(n):
    n=n+1
k=10
print("k=",k)
modify(k)
print("k=",k)

def modify(msg):
    msg += ' to you. '
    print('Inside :',msg)
    return
msg = 'happy birthday'
print('Before:',msg)
modify(msg)
print('After:',msg)

#키워드 인수
def func(name,age):
    print('Name:',name)
    print('Age:',age)
    return
func(age=27,name = 'Tom')

#디폴트 인수
def greet (name,msg="별일없죠?"):
    print("안녕 ",name+', '+msg)
greet("영희")

def sayHello(name = 'Everybody'):
    s='Hello! ' +name
    return s
print(sayHello())
print(sayHello('John'))

#키워드 & 디폴트 인수 사용
def getSum(end,begin=1):
    result =0
    for i in range(begin,end+1):
        result+= i
    return result
print('15까지 합:',getSum(15))
print('3~25까지의 합:',getSum(25,3))
print('3~25까지의 합: ' ,getSum(begin=3,end=25))

