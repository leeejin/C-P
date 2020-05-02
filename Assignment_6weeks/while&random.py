#while문
n=1
sum=0
while n<=10:
    sum=sum+n
    n=n+1
print("1~10까지의 합:",sum)

n=1
sum=0
while sum<=500:
    n=n+1
    sum=sum+n
print("1~",n,"까지의 합:",sum)

#random함수
import random
n=0
while n!=4:
    n = random.randint(0,9)
    print(n)

#random함수 예제
print("1~100사이의 숫자를 맞추시오")
count=0
n=0
idk = random.randint(1,100)
while n!=idk:
    n = int(input("숫자 입력 : "))
    count=count+1
    if n<idk:
            print("높음!")
    elif n>idk:
            print("낮음!")
print(count,"번째",n,"찾음.")
