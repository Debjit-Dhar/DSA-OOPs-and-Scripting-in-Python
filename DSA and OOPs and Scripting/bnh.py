import math
def anytodec(n,b):
    i,s=0,0
    for i in range(len(n)):
        if(n[i].isalpha()):
            s+=int(math.pow(b,len(n)-i-1)*(ord(n[i])-55))
        else:
            s+=int(math.pow(b,len(n)-i-1)*int(n[i]))
    return s
n=input('Enter')
b=8
print(anytodec(n,b))