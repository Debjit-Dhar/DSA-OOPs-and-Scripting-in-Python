import numpy as np
import matplotlib.pyplot as pl
def f(x,y):
    return -x*y
def fsol(x):
    return np.exp(-(x*x)/2)
x1,y1,xf=float(input('Enter x1')),float(input('Enter y1')),float(input('Enter xf'))
h,x2,y2=0.5,0,0
i=0
x,y=x1,y1
X=np.arange(x1,xf+h,h)
n=int((xf-x1)/h)+1
L=[0 for i in range(n)]
pl.plot(X,fsol(X),label='True Solution')
#Euler's Method
while(x1<=xf):
    L[i]=y1
    x2=x1+h
    y2=y1+h*f(x1,y1)
    x1=x2
    y1=y2
    i+=1
Y=np.array(L)
print(X)
print(Y)
pl.plot(X,Y,label='Eulers Method')
#Heun's Method
i=0
L=[0 for i in range(n)]
x1,y1=x,y
while(x1<=xf):
    L[i]=y1
    x2=x1+h
    y2=y1+h*f(x1,y1)
    y2=y1+h*(f(x1,y1)+f(x2,y2))/2
    x1=x2
    y1=y2
    i+=1
Y=np.array(L)
print(Y)
pl.plot(X,Y,label='Heuns Method')
#Midpoint's Method
i=0
L=[0 for i in range(n)]
x1,y1=x,y
while(x1<=xf):
    L[i]=y1
    x2=x1+h
    y2=y1+h*f(x1,y1)
    y2=y1+h*(f((x1+x2)/2,(y1+y2)/2))
    x1=x2
    y1=y2
    i+=1
Y=np.array(L)
print(Y)
pl.plot(X,Y,label='Midpoints Method')
pl.legend()
pl.show()
