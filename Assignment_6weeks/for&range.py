words =['happy','sunday','bay','pretty']
c=0
for id in words:
    if 'ay' in id:
        print(id)
        c=c+1
print(len(words),'개의 원소중',c,'개 발견 \n')

#문자열활용 for문
for c in "abcdef":
    print(c,end=' ')

#문자열 활용 예제
w = input('단어입력:')
cnt =0
for c in w:
    if c not in 'aeiouAEIOU':
        cnt=cnt+1
        print(c,end=' ')
print('\n'+w+'의 자음수: ' ,cnt,'\n')

#range() 함수 활용 for문
#range(10) : 0부터 9까지를 의미함(range(0,10))
#10번 반복
#sum 변수에 0부터 9까지 차례로 더함
sum=0
for x in range(10):
    sum = sum+x
print(sum,'\n')

num = int(input('정수 입력:'))
star = '*'
tstar = ''
for i in range(num):
    tstar = tstar +star
    print(tstar)
