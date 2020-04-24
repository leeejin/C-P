n1 = int(input('자연수1:'))
n2 = int(input('자연수2:'))
if n1>n2:
    print('목:',n1/n2,'나머지:',n1%n2)
    if n2==0:
        print('Divide by zero')

if n2>n1:
    print('목:',n2/n1,'나머지:',n2%n1)
    if n1==0:
        print('Divide by zero')
