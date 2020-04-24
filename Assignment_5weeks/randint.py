import random
a = int(input('1~10 정수 입력: '))
x = random.randint(1,10)
if x==a:
    print('성공')
else:
    print('실패')
