def merge(a,l,m,r):
    n1,n2 = m - l + 1, r - m
    L,R=[0]*n1,[0]*n2
    for i in range(n1):
        L[i] = a[l + i]
    for j in range(n2):
        R[j] = a[m + 1 + j]
    i,j,k=0,0,l
    while (i < n1 and j < n2):
        if (L[i] <= R[j]):
            a[k] = L[i]
            k+=1
            i+=1
        else:
            a[k] = R[j]
            k+=1
            j+=1
    while (i < n1):
        a[k] = L[i]
        k+=1
        i+=1
    while (j < n2):
        a[k] = R[j]
        k+=1
        j+=1
def msort(a,l,r):
    if (l < r):
        m = l + (r - l) // 2
        msort(a, l, m)
        msort(a, m + 1, r)
        merge(a, l, m, r)
a=[4,-2,1,-2,3]
n=len(a)
msort(a,0,n-1)
print(a)