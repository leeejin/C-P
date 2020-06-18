#빈 집합 생성 시 set()함수 사용
st3=set()
print('st3:',st3,type(st3))
st3.add(11)
print('st3:',st3)
#add() 연산 시, 집합에 값이 추가됨
#리스트나 튜플,문자열을 집합으로 변환
st4=set([1,2,3,4])
st5=set('abracadabra')
print('st4:',st4)
print('st5:',st5)
#집합에서는 순서가 의미 없음
#   사용 예        결과
#len({1,1,2,3})     3
#3 in {1,2,3}       True
#sum{1,2,10}        13
#{1,2,3}=={2,3,1}   True

#집합 연산 : 비교 연산
st6 = {1,2,3,4,5,6}
st7={1,3,5}
print(st6>st7)

#합집합,교집합,차집합
sa={1,3,5}
sb={1,2,4}
print(sa&sb)
print(sa.union(sb))
print(sa-sb)
#집합 삭제
#discard() : 지우려는 원소있으면 삭제. 없으면 아무일도 없음
#remove() : 지우려는 원소있으면 삭제. 없으면 error
st = {'a','b','c'}
st.discard('a')
print(st)

#집합 : 예제
c=input("문자열 입력: ")
s=set(c)
for k in s:
    i=0
    for n in c:
        if k==n:
            i+=1
    print(k,':',i,'회')

stmt = '''Time is
    Too Slow for those who Wait
    Too Swift for those who Fear
    Too Long for those who Grieve
    Too Short for those who Rejoice
    But for those who love
    Time is not'''
print('문장:\n',stmt)
words=set()
wordList=stmt.split()
for word in wordList:
    words.add(word.lower())
print('단어 수:',len(words))
print(words)

#사전생성
grade = {"eng":87,"math":98}
dcEmpty={}
print(grade,type(grade))
print(dcEmpty)

#함수 dict() 이용하여 사전생성
#키-값 쌍의 리스트나 파라미터 형태로부터 사전생성
phone = dict([("부산",51),("서울",2)])
empno=dict(Tom=4221,Jack=3345)
print(phone)
print(empno)

#for문 활용 : 임의의 키와 값을 나타내는 수식으로 사전 생성
numSquare = {x:x**2 for x in (3,5,7)}
print(numSquare)

#사전 검색 : dicName[key] but 키가 없으면 KeyError 오류 발생
grade = {"eng":87,"math":98}
print(grade["math"])

#사전 추가
#dicName[key] = value
grade = {"eng":87,"math":98}
grade["sci"]=95
grade[100]="kor"
print(grade)

#사전 갱신
grade = {"eng":87,"math":98,"sci":95}
grade["sci"]=94
print(grade)

#사전 삭제 : del dictName[key]
grade = {"eng":87,"math":98,"sci":95}

del grade["math"]
print(grade)

#모든 항목 삭제 : clear()
grade = {"eng":87,"math":98,"sci":95}
grade.clear()
print(grade)

#사전 전부 삭제
#grade = {"eng":87,"math":98,"sci":95}
#del grade
#print(grade)


#사전 연산
#       사용 예                결과
#len({"eng":87,"math":98})      2
#"eng" in {"eng":87,"math":98}  True
#{1:"ㅇ",2:"t"}=={2:"t",1:"ㅇ"} True

#dct.clear() : 사전 dct의 모든 항목제거
#dct.copy() : 사전 dct의 복사본을 반환
#dct.keys() : 사전 dct의 키들이 리스트를 반환
#dct.values() : 사전 dct의 값들이 리스트를 반환
#dct.items() : 사전 dct의 (키,값) 쌍 튜플들의 리스트를 반환
#dct.update(dct2) : 사전 dct2의 항목들을 사전 dct에 추가
#dct.get(key) : 사전 dct의 키 key에 대한 값을 반환
#dct.pop(key) : 사전 dct의 키 key 에 대한 값을 반환하고 항목 제거

#메소드 활용 예제
grade = {"eng":87,"math":98}
print("key:",grade.keys())
print("value:",tuple(grade.values()))

grade = {"eng":87,"math":98}
for k,v in grade.items():
    print(k,v)

grade = {"eng":87,"math":98}
grd2={"kor":87,"sci":95}
grade.update(grd2)
print(grade)

#첫 GUI 프로그래밍
#import tkinter
#top = tkinter.TK()
#top.mainloop()
