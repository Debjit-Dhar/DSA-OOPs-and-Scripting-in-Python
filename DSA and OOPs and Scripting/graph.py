import matplotlib.pyplot as pl
import math
import numpy as np
def f(x):
    return x*x*x
a=float(input('Enter start '))
b=float(input('Enter end '))
ch=int(input("Enter choice 1 for algebraic and 2 for non-algebraic "))
xpoints=np.arange(a,b,0.00001)
if ch==1:
    ypoints=f(xpoints)
else:
    ypoints=np.sin(xpoints)
pl.title('GRAPH OF GIVEN FUNCTION')
pl.plot(xpoints,ypoints,label='f(x)')
pl.grid()
pl.legend()
pl.show()
