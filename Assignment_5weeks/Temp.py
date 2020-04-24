temp = int(input('현재 온도는?'))
print('\n오늘은',end =' ')
if temp<0:
    temp= -temp
    print('영하', end=' ')
print(temp,'도입니다.')
