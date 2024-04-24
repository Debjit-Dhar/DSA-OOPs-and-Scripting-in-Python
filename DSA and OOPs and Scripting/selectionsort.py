L=[4,-2,1,-2,3]
n=len(L)
for i in range(n):
    small,pos=L[i],i
    for j in range(i+1,n):
        if L[j]<small:
            small,pos=L[j],j
    L[pos],L[i]=L[i],small
print(L)
