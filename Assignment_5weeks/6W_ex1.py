age = int(input('나이는?'))
mon = int(input('요금은?'))
if age>=65:
    print('요금은',mon * 50/100,'입니다')
else:
    print('요금은',mon,'입니다')
