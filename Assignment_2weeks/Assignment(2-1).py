number = int(input("세자리 정수 입력: "))
hundred = number//100
ten = number%100 //10
one = number %100 %10 //1
print("입력한 수의 역순: ",one,ten,hundred)
