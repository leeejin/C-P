import random
num = int(input('사용자 수 선택:'))
print('사용자:',num,'\t')
x = '짝'
y = '홀'
com = random.randrange(2)
if com == 0:
    print('컴퓨터:',x)
    if num %2==0:
        print('==> 컴퓨터 승')
    else:
        print('==> 사용자 승')
else:
    print('컴퓨터:',y)
    if num %2==0:
        print('==> 사용자 승')
    else:
        print('==> 컴퓨터 승')
