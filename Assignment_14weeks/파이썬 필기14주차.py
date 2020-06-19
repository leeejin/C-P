#파이썬에서는 모든 데이터가 객체
#객체의 타입은 클래스에 의해 정의
s= 'Python'
print(type(s))
#문자열에 대한 클래스:str
#정수에 대한 클래스:int
#실수에 대한 클래스:float
#리스트에 대한 클래스:list

#객체에 대한 설계도:클래스(class)
#클래스 생성위한 문법
#class ClassName:
#    stmt-1
#    ...
#    stmt-n
#클래스의 몸체에 pass문장만 있는 경우
#두 개의 객체 생성
class Emp:
    pass
x=Emp()
y=Emp()
print(x==y)
#일반적으로 속성은 클래스 내부에서 정의
#존재하는 객체에서 동적으로 속성 생성
class Emp:
    pass
x=Emp()
y=Emp()
x.name='James'
x.age=37
print('Name:',x.name,'\nAge:',x.age)
print('x_dict_:',x.__dict__)
print('y_dict_:',y.__dict__)
#__dict__:각 객체가 가지고 있는 사전형 속성과 값
#객체는 속성 공유
class Emp:
    pass
x=Emp()
y=Emp()
Emp.dept = 'Research'   # case 1
print('xDept:',x.dept,'\tDept:',y.dept)
x.dept = 'Accounting'   # case 2
print('xDept:',x.dept,'\tclassDept:',Emp.dept)
Emp.dept='Sales'        # case 3
print('xDept:',x.dept,'\tyDept:',y.dept)
print('x__dict__:',x.__dict__)
print('y__dict__:',y.__dict__)


#객체 속성 연결
def f(x):
    return 42
print(type(f))
f.x=47
print(f(5)) #f() : 함수 호출
print(f.x)  #f.x : 함수명의 속성 

#클래스 메소드
#객체를 인수로 하는 함수 intro() 정의
def intro(emp):
    print('My name is',emp.name,'!')
class Emp:
    pass
a = Emp()
a.name = 'John'
intro(a)

#함수 intro()를 클래스 속성인 myIntro에 연결
def intro(emp):
    print('My name is',emp.name,'!')
class Emp:
    myIntro =intro
a=Emp()
a.name='John'
Emp.myIntro(a)

#함수를 클래스 내부에서 정의:메소드
class Emp:
    def myIntro(emp):
        print('My name is',emp.name,'!')
a=Emp()
a.name='John'
a.myIntro()

#메소드 정의 및 활용
class Emp:
    def restart(self):
        self.bonus=0
    def sale(self):
        self.bonus+=10
a=Emp()
a.name='James'
a.restart()
a.sale()
print(a.name+'의 보너스는',a.bonus)

#클래스 : 예
class Counter:
    def reset(self):
        self.count=0
    def increment(self):
        self.count+=1
    def get(self):
        return self.count
a=Counter()
a.reset()
a.increment()
print("카운터 a의 값은",a.get())
#생성자 : 객체가 생성될 때 객체를 기본값으로 초기화하는 특수한 메소드
#메소드 : __init__()
class Emp:
    def __init__(self):
        print('__init__실행')
a=Emp()
#앞의 Emp 클래스에 __init__()메소드 추가
class Emp:
    empTotal=0
    def __init__(self,name,bonus=100):
        self.name=name
        self.bonus = self.base = bonus
        Emp.empTotal +=1
    def restart(self):
        self.bonus = self.base
    def sale(self):
        self.bonus += 10
        
a = Emp('Peter',50)
b = Emp('Austin')
a.sale()
print(a.name + '의 보너스:',a.bonus)
print(b.name + '의 보너스:',b.bonus)
print('총 직원 수:',Emp.empTotal)

#__str__() 메소드
class Emp:
    empCnt=0
    def __init__(self,name,bonus=100):
        self.name=name
        self.bonus = self.base = bonus
        Emp.empCnt +=1
    def __str__(self):
        return '이름: '+self.name+' 보너스: '+str(self.bonus)
    def restart(self):
        self.bonus = self.base
    def sale(self):
        self.bonus +=10
a=Emp('Peter',50)
a.sale()
print(a)

#정보은닉
class Emp:
    empCnt=0
    def __init__(self,name,bonus=100):
        self.name=name
        self.bonus=bonus
print()
a = Emp('Peter')
a.bonus = 150
print(a.bonus)
#클래스의 내부 변수를 마음대로 변경 가능
#private 변수 이용하여 외부로부터 차단 : 변수 앞에 __붙임
#class Emp:
#    empCnt=0
#    def __init__(self,name,bonus=100):
#        self.name=name      #public 속성
#        self.__bonus=bonus  #private 속성
#a=Emp('Peter')
#print('이름:',a.name)
#print('보너스:',a.__bonus)
#       ->오류 뜸 외부에서 접근을 차단했기때문

#접근자와 설정자
class Emp:
    empCnt =0
    def __init__(self,name,bonus=100):
        self.__name=name
        self.__bonus = self.__base=bonus
        Emp.empCnt +=1
    def restart(self):
        self.__bonus += 10
    def sale(self):
        self.__bonus +=10
    def getName(self):
        return self.__name
    def getBonus(self):
        return self.__bonus
a = Emp('Peter',50)
a.sale()
print('이름:',a.getName(),end=' ')
print('보너스:',a.getBonus())

#연습문제
class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def getArea(self):
        return self.width * self.height
    def getPerimeter(self):
        return self.width * 2 + self.height * 2
a = Rectangle(1,1)
print('사각형의 넓이는',a.getArea())
print('사각형의 둘레는',a.getPerimeter())

#파일 처리 과정
#f = open(filename,mode) : 파일을 열다
#readDate = f.read() : 파일에서 데이터를 읽거나 쓸 수 있다.
#f.close() : 파일과 관련된 작업이 모두 종료되면 파일을 닫아야 한다.

#fp = open('foo.txt','w')
#print('Name:',fp.name)
#print('Mode:',fp.mode)
#print('Closed:',fp.closed)


#파일 읽기
#read() 메소드 : 열린 파일로부터 모든 데이터 읽고, 하나의 문자열로 반환
fp = open('song.txt','r')
print('<<song.txt 전부 읽기>>')
rfile = fp.read()
print(rfile)
print('<<song.txt 부분 읽기 [2:5]>>')
print(rfile[2:5])
fp.close()

#read(n) 메소드 : n개의 문자를 읽고 문자열로 반환
#다음 읽기를 위해 파일 포인터의 위치를 읽은 다음의 위치 설정
fp = open('song.txt','r')
print('<<song.txt 일부 읽기>>')
c15 = fp.read(15)
print(c15)
print('<<song.txt 계속 읽기>>')
next = fp.read()
print(next)
fp.close()
#readline() 메소드 : 파일로부터 \n으로 끝나는 한 줄씩만 읽음
fp= open('song.txt','r')
line1 = fp.readline()
line2 = fp.readline()
print('<<song.txt 한줄씩 읽기>>')
print(line1)
print(line2)
fp.close()
#readlines() 메소드 : 파일로부터 모든 줄을 읽고, 각 줄의 문자열을 항목으로 하는 list로 반환
fp = open('song.txt','r')
lines = fp.readlines()
print(lines)
fp.close()
#list의 각 항목을 나타내기 위해 인덱스 사용
fp = open('song.txt','r')
lines = fp.readlines()
print(lines[0])
print(lines[1])
fp.close()
#open() 함수 : 존재하지 않는 파일에 대해 읽기 모드로 함수 open() 시행 시, FileNoFoundError 오류 발생

#한 줄씩 읽기
#for문을 이용하여 모든 줄 읽음
#한번에 한 줄씩 처리함
#rstrip() 이용 줄바꿈 문자(\n)잘라냄
fp= open('song.txt','r')
for line in fp:
    st = line.rstrip()
    print(st)
fp.close()

#with 키워드 : close() 명령 필요없음
with open('song.txt','r') as fp:
    rfile = fp.read()
    print(rfile)
print('Closed:',fp.closed)

#write() 메소드 : 파일에 문자열을 씀(w), 문자열 출력시 한 줄의 끝마다 \n 추가해야 함
fp = open('song1.txt','w')
n = fp.write('Yesterday once more\nDust in the wind\n')
print(n,'문자 writing')
fp.close()

#파일 추가
#기존 파일에 문자열을 추가할 때, 추가모드(a) 사용함
fp = open('song1.txt','a')
fp.write('Yesterday\nWithout you\n')
fp.close()

#파일 활용
#split() 함수 : 문장을 단어 list로 분리
#파일로부터 모든 문자열을 읽어서 단어의 리스트로 분할
ifp = open('song.txt','r')
ofp = open('songWord.txt','a')
for fline in ifp:
    line = fline.strip()
    wordList = line.split()

    for word in wordList:
        ofp.write(word+'\n')
ifp.close()
ofp.close()

#프로그램
fname = input("파일명 입력:")
fp = open(fname,'r')
line =0
for stLine in fp:
    line += 1
    print('\n<<< line',line,'>>>',stLine.strip())
    st = set(stLine)

    for k in st:
        if k==' ' or k=='\n':
            continue
        i=0
        for n in stLine:
            if k == n:
                i+=1
        print(k+':'+str(i),end='; ')
    print()
fp.close()

#연습문제
