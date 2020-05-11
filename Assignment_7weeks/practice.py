lst = [28,13,76,32,63]
def listmax(lst):
        return lst
print(lst,'max= ' ,max(lst))

#예제
def main():
        print(power(10,2))
def power(x,y):
        result =1
        for i in range(y):
                result = result *x
        return result
main()

#예제
def CtoF(c):
        F = 9 / 5 * c + 32
        return F
deg = eval(input('섭씨 온도: '))
print('화씨 온도:',CtoF(deg))

#실습
n = int(input('정수입력:'))
def square(n):
       return n * n
print(square(10))

#실습2
x = int(input('정수입력1:'))
y = int(input('정수입력2:'))
def getPower(x,y):
        sum =1
        for i in range(y):
                sum *=x
        return sum
print(getPower(8,3))
