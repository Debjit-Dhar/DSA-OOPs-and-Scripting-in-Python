L=[4,-2,1,-2,3]
n=len(L)
for i in range(1,n):
    temp=L[i]
    j=i-1
    while j>=0 and temp<L[j]:
        L[j+1]=L[j]
        j-=1
    L[j+1]=temp
print(L)
