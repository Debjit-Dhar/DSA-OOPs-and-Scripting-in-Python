lfp1,lfp2=float(input('Enter lfp of first scale')),float(input('Enter lfp of second scale'))
ufp1,ufp2=float(input('Enter ufp of first scale')),float(input('Enter ufp of second scale'))
fi1,fi2=ufp1-lfp1,ufp2-lfp2
t1=float(input('Enter temperature in first scale'))
t2=(fi2/fi1)*(t1-lfp1)+lfp2
print("Temperature in second scale is",t2)