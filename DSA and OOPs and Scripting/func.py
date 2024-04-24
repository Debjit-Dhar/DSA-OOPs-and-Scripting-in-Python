from scipy import optimize
import math
def f(x):
    return x+math.cos(x)
r=optimize.root(f,0)
m=optimize.minimize(f,0,method='BFGS')
#M=optimize.maximize(f,0)
print(r.x)
print(m.x)
#print(M)