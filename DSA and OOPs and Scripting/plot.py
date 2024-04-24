from cProfile import label
from numpy import arange
from pandas import read_csv
from scipy.optimize import curve_fit
from matplotlib import pyplot


""" 
def orgFn(x):
	return 8.5*x + 1

def orgFnODE(x, y):
	return 8.5
"""

""" 
def orgFn(x):
	return - 10*x**2 + 8.5*x + 1

def orgFnODE(x, y):
	return - 20*x + 8.5
"""

""" 
def orgFn(x):
	return 4*x**3 - 10*x**2 + 8.5*x + 1

def orgFnODE(x, y):
	return 12*x**2 - 20*x + 8.5
"""

#""" 
def orgFn(x):
	return -0.5*x**4 + 4*x**3 - 10*x**2 + 8.5*x + 1

def orgFnODE(x, y):
	return -2*x**3 + 12*x**2 - 20*x + 8.5
#"""



def euler(x1, y1, h, xf):
	print('Euler\'s Method')
	euler_x_line=[]
	euler_y_line=[]
	euler_x_line.append(x1)
	euler_y_line.append(y1)
	print(x1, y1)
	while(x1<xf):
		x2=x1+h
		y2=y1+h*orgFnODE(x1, y1)
		euler_x_line.append(x2)
		euler_y_line.append(y2)
		x1=x2
		y1=y2
		print(x1, y1)
	return euler_x_line, euler_y_line

def heun(x1, y1, h, xf):
	print('Heun\'s Method')
	heun_x_line=[]
	heun_y_line=[]
	heun_x_line.append(x1)
	heun_y_line.append(y1)
	print(x1, y1)
	while(x1<xf):
		s1=orgFnODE(x1, y1)
		x2=x1+h
		y2=y1+h*s1
		s2=orgFnODE(x2, y2)
		y2=y1+h*(s1+s2)/2
		heun_x_line.append(x2)
		heun_y_line.append(y2)
		x1=x2
		y1=y2
		print(x1, y1)
	return heun_x_line, heun_y_line

def midpoint(x1, y1, h, xf):
	print('Midpoint Method')
	mp_x_line=[]
	mp_y_line=[]
	mp_x_line.append(x1)
	mp_y_line.append(y1)
	print(x1, y1)
	while(x1<xf):
		xh2=x1+h/2
		yh2=y1+h*orgFnODE(x1, y1)
		x2=x1+h
		y2=y1+h*orgFnODE(xh2, yh2)
		mp_x_line.append(x2)
		mp_y_line.append(y2)
		x1=x2
		y1=y2
		print(x1, y1)
	return mp_x_line, mp_y_line

def RK_4(x1, y1, h, xf):
	print('Fourth Order RK Method')
	mp_x_line=[]
	mp_y_line=[]
	mp_x_line.append(x1)
	mp_y_line.append(y1)
	print(x1, y1)
	while(x1<xf):
		k1=orgFnODE(x1, y1)
		k2=orgFnODE(x1+h/2, y1+k1*h/2)
		k3=orgFnODE(x1+h/2, y1+k2*h/2)
		k4=orgFnODE(x1+h, y1+k3*h)
		x2=x1+h
		y2=y1+(k1+2*k2+2*k3+k4)*h/6
		mp_x_line.append(x2)
		mp_y_line.append(y2)
		x1=x2
		y1=y2
		print(x1, y1)
	return mp_x_line, mp_y_line

x_left=0
x_right=4
y_at_x_left=1


step_size=0.1
x_line = arange(x_left, x_right+step_size, step_size)
y_line = orgFn(x_line)
yd_line = orgFnODE(x_line, y_line)


line_color='blue'
#pyplot.scatter(x_line, y_line, color=line_color)
pyplot.plot(x_line, y_line, color=line_color, label='f(x)')

#"""
step_size=0.5
step_count=1
i=1
while(i<=step_count):
	x_line, y_line = euler(x_left, y_at_x_left, step_size, x_right)
	line_color='red'
	line_label='Euler (h='+str(step_size)+')'
	pyplot.scatter(x_line, y_line, color=line_color)
	pyplot.plot(x_line, y_line, color=line_color, label=line_label)
	step_size=step_size/2
	i+=1
#"""

#"""
step_size=0.5
step_count=1
i=1
while(i<=step_count):
	x_line, y_line = heun(x_left, y_at_x_left, step_size, x_right)
	line_color='green'
	line_label='Heun (h='+str(step_size)+')'
	pyplot.scatter(x_line, y_line, color=line_color)
	pyplot.plot(x_line, y_line, color=line_color, label=line_label)
	step_size=step_size/2
	i+=1
#"""

#"""
step_size=0.5
step_count=1
i=1
while(i<=step_count):
	x_line, y_line = midpoint(x_left, y_at_x_left, step_size, x_right)
	line_color='cyan'
	line_label='Midpoint (h='+str(step_size)+')'
	pyplot.scatter(x_line, y_line, color=line_color)
	pyplot.plot(x_line, y_line, color=line_color, label=line_label)
	step_size=step_size/2
	i+=1
#"""

#"""
step_size=0.5
step_count=1
i=1
while(i<=step_count):
	x_line, y_line = RK_4(x_left, y_at_x_left, step_size, x_right)
	line_color='magenta'
	line_label='RK-4 (h='+str(step_size)+')'
	pyplot.scatter(x_line, y_line, color=line_color)
	pyplot.plot(x_line, y_line, color=line_color, label=line_label)
	step_size=step_size/2
	i+=1
#"""

pyplot.legend()
pyplot.show()

solveODE.py
