# n= 자연수 개수
# m= 계산 횟수
# k= 같은 숫자가 반복될 최대수 
# 까지를 공백으로 구분하여 입력받기
n,m,k = map(int,input().split())

# n개의 수를 공백으로 구분하여 입력받기
data = list(map(int,input().split()))

data.sort() # 정렬
first = data[n-1] # 가장 큰 수
second = data[n-2] # 두번째로 큰 수

# 가장 큰수가 더해지는 횟수 계산
count = int(m/(k+1))*k # m/(k+1)로 나눈 몫이 수열이 반복되는 횟수 * k = 가장 큰 수가 등장하는 횟수
count += m % (k+1) # 위에서 나누어 떨어지지 않을 경우, 나눈 몫의 나머지만큼 가장 큰 수를 추가로 더함

result = 0
result += (count) * first # 가장 큰 수 더하기
result += (m-count) *second # 두 번째로 큰 수 더하기

print(result)