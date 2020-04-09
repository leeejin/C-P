first = input("이름 첫째자는: ")
second = input("이름 둘째자는: ")
third = input("이름 셋째자는: ")
first1 = chr(ord(first[0])+32)+first[1:]
second1 = chr(ord(second[0])+32)
third1 = chr(ord(third[0])+32)
print("***********")
print(second1+third1+first1)
