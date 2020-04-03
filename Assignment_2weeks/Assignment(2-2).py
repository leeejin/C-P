birthday = int(input("생일 : "))
n1 = birthday // 1000
n2 = birthday % 1000 // 100
n3 = birthday % 1000 % 100 // 10
n4 = birthday % 1000 % 100 % 10 // 1
total = n1+n2+n3+n4
print(total)
