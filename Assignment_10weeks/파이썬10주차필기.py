#무명함수 : lambda
#lambda function define
mul = lambda arg1,arg2: arg1*arg2
#function call
print('곱셈 값:',mul(10,20))
print('곱셈 값:',mul(37,29))
#중첩 함수를 정의하기 위해 lambda함수 사용
def nestfunc(n):
    return lambda x:x*n
dbl = nestfunc(2) #dbl = lambda x: x*2
tri = nestfunc(3) #tri = lambda x: x*3
print(dbl(25))
print(tri(10))
#지역변수의 범위 : 지역변수는 함수 안에서만 사용 가능
#def cArea(radius):
#    result = 3.14 * radius **2
#    return result
#r = float(input("원의 반지름: "))
#area = cArea(r)
#print(result) -> 컴파일 에러
#전역변수 : 전역변수는 어디서나 사용할 수 있다
def cArea():
    result = 3.14 *r**2
    return result
r = float(input("원의 반지름: "))
area = cArea()
print(area)
#함수 안에서 전역 변수 변경
def cArea(radius):
    area = 3.14 * radius **2
    return
area =0
r = float(input("원의 반지름: "))
cArea(r)
print(area)
#0이 나오는 이유는? def 안의 area는 새로운 지역 변수 area가 생성된 나머지 area는 global
#global 사용
def cArea(radius):
    global area
    area = 3.14 * radius **2
    return
area =0
r = float(input("원의 반지름: "))
cArea(r)
print(area)
#전역 변수
def func():
    s='Banana'
    print(s)
s='Apple'
func()
print(s)
#함수 내에서는 지역변수, 호출 후에는 전역변수 참조
#전역 변수를 함수 안에서 사용
def func():
    global s
    print(s)
    s='Banana'
    print(s)
s='Apple'
func()
print(s)
#함수 내부의 첫 print()문 시행 전에 지역변수를 참조하지 않았으나, s를 global로 선언함으로서 전역변수 사용
#두번째 print()문 시행 전 변수 s에 'banana'가 할당되어 전역 변수의 값이 변함

#예제
def sub(x,y):
    global a
    a=7
    x,y=y,x
    b=3
    print(a,b,x,y)
a,b,x,y=1,2,3,4
sub(x,y)
print(a,b,x,y)

#순서형 자료구조
#리스트(list): 여러 개의 데이터가 저장되어 있는 장소 []
lst1 = [1,2,3,4]
#튜플(tuple):리스트와 유사한 순서형 구조,()
tup1 = (1,2,3,4,5)
#집합(set):수학의 집합 개념과 동일,{}
st1={1,2,4}
#사전(dict):키와 값의 쌍으로 저장,{}
dic1 = {1:'one',2:'two',4:'four'}
#튜플(tuple)
tup51='hello'
tup61='hello',
print('tup51:',tup51)
print('tup61:',tup61)
#tuple함수 사용
#다른 순서형 자료(리스트나 문자열)로부터 튜플 구
tup7=tuple([1,2,3,4])
tup8=tuple('Python')
print('tup7 :',tup7)
print('tup8 :',tup8)
#튜플을 변수에 할당
tup9=(19001,'Tom','A')
num,name,grade = tup9
print(name,grade,num)
#튜플 예제 : 정사각형의 넓이와 둘레를 튜플로 반환
def square(length):
    area = length * length
    circum = 4 * length
    return (area,circum)
radius = int(input("한 변의 길이: "))
tupVal = square(radius)
print("넓이:",tupVal[0]," 둘레:",tupVal[1])
#튜플연산: 인덱스연산과 슬라이싱
tup2=(1,4,9,16,25)
tup3='a','b','x','y','z'
x=tup2[3]
print('tup2[3]:',x)
print('tup3[:3]',tup3[:3])
#튜플 처리위한 내장함수
#cmp(t1,t2) : 두 튜플의 원소를 비교
#len(t) : 튜플 t의 길이(원소의 개수)
#min(t) : 튜플 t의 가장 작은 원소
#max(t) : 튜플 t의 가장 큰 원소
#tuple(seq) : 리스트나 문자열 등을 튜플로 변환

#튜플의 갱신과 삭제
#변경할 수 없는 순서형 자료구조
#원소의 값을 바꾸거나, 추가하거나 삭제할 수 없음
#기존의 튜플에 새로운 튜플 할당은 가능
tup1 = (1,4,9,16,25)
tup1= 'a','b','c'
print(tup1)
#임의의 원소를 지우는건 불가능
#튜플 전체를 지우는 것은 del 명령어로 가능
tup1=(1,4,9,16,25)
del tup1 #튜플 삭제된거임
#튜플: 연습문제
var1=(1,4,9,16,25)
var2='x','y','z'
var1=var1+var2
print(var1,var2)

var3=(1,4,9,16,25)
var4='x','y','z'
var3=var3+var4
print(var3,var4)

var5=(1,4,9,16)
var6=(4,16,1,9)
print(var5==var6)

var7=(1,4,9,16)
var8=(4,16,1,9)
print(var7<var8)

var9=('Hello')*3
var10=('Hello',)*3
