import numpy as np
import matplotlib.pyplot as plt
import math

x=np.arange(0,10,0.1)
y1 = 0.1*(x**2)+1
y2 = np.zeros(100)
for i in range(0,100):
    y2[i]=math.exp(0.1*x[i])

y3=np.zeros(100)
for i in range(0,100):
    y3[i]=math.sin(x[i])

plt.plot(x,y1,'k',label='graph1 y1=0.1*x^2+1')
plt.plot(x,y2,'r',label='graph2 y2=exp(0.1*x)')
plt.plot(x,y3,'--m',label='graph3 y3=sin(x)')

plt.xlabel('x')
plt.ylabel('y')

plt.legend(loc=2)
plt.title('complicated graph')
plt.show()
