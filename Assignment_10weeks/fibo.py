#Fibonacci 수 모듈 : fibo.py

def nfib(n):            #n-번째 Fibonacci 수
    a,b = 0,1
    k=1
    while k<=n:
        a,b=b,a+b
        k=k+1
    return a
def fib(n):             #n-번째 Fibonacci 수
    result =[]
    a,b = 0,1
    k=1
    while k<= n:
        result.append(b)
        a,b = b, a+b
        k= k+1
    return result
