#Fibonacci 수 모듈 : fibon.py

def fib(n): #n-번째까지의 Fibonacci 수열
    result =[]
    a,b = 0,1
    k=1
    while k<=n:
        result.append(b)
        a,b = b, a+b
        k = k+1
    return result
if __name__ =="__main__":
    f= fib(12)
    print(f)
