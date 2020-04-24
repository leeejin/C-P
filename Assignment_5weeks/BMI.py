weight = int(input('몸무게는:'))
height = int(input('키는:'))
height *= 0.01
BMI = weight / (height * height)
print('당신의 BMI:',BMI)
if BMI>=30:
    print('비만')
elif BMI>= 25:
    print('과제충')
elif BMI>=18.5:
    print('정상')
else:
    print('저체중')
