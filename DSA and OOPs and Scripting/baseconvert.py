import math
def dectoany(n,b):
    s=""
    while(n>0):
        d=n%b
        n//=b
        if d>9:
            s=chr(55+d)+s
        else:
            s=str(d)+s
    return s
def anytodec(n,b):
    i,s=0,0
    for i in range(len(n)):
        if(n[i].isalpha()):
            s+=int(math.pow(b,len(n)-i-1)*(ord(n[i])-55))
        else:
            s+=int(math.pow(b,len(n)-i-1)*int(n[i]))
    return s
b1=int(input('Enter base of number'))
b2=int(input('Enter base to be converted to'))
n=input('Enter number')
s=anytodec(n,b1)
print(dectoany(s,b2))
sent=input('Enter string')
i=0
for i in range(len(sent)):
    print(dectoany(ord(sent[i]),2),end='\t')