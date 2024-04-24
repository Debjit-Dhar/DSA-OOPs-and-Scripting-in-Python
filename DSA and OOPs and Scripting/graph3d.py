from mpl_toolkits import mplot3d
import matplotlib.pyplot as pl
import numpy as np
def f(x,y):
    return x*x+np.sin(y*y)
a=float(input('Enter Start'))
b=float(input('Enter End'))
x=np.linspace(a,b,100)
y=np.linspace(a,b,100)
X,Y=np.meshgrid(x,y)
Z=f(X,Y)
fig=pl.figure()
ax=pl.axes(projection='3d')
ax.plot_surface(X,Y,Z,rstride=1, cstride=1,cmap='jet', edgecolor = 'none')
pl.title('Graph of given 2 variable function')
pl.show()