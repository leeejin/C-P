import testModule
tm = testModule.sayHi('길동')
print(tm)
#모듈활용
#일반적 방법
import random
random.randint(1,10)
#사용시 생략할 수 있는 방법
from random import *
randint(1,10)
#약어 사용방법
import random as r
r.randint(1,10)
