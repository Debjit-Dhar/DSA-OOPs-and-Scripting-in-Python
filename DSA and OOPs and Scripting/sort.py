L=[4,-2,1,-2,3]
n=len(L)
i=n-1
for i in range(n):
    for j in range(i):
        if L[j]>L[j+1]:
            L[j],L[j+1]=L[j+1],L[j]
print(L)