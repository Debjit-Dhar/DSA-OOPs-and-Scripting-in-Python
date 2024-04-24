from scipy import optimize
import math
def f(x):
    return x+math.cos(x)
r1=optimize.root(f,0)
print(r1)
print("The root is= ",r1.x)