def qsort(a,l,r):
    l1,r1,pivot=l,r,a[l]
    while(l<r):
        while(a[r]>=pivot and l<r):
            r-=1
        if(l!=r):
            a[l]=a[r]
            l+=1
        while(a[l]<=pivot and l<r):
            l+=1
        if(l!=r):
            a[r]=a[l]
            r-=1
    a[l],pivot,l,r=pivot,l,l1,r1
    print('0 call', a, l, r)
    if(l<pivot):
        print('1 call', a, l, r)
        qsort(a,l,pivot-1)
    if(r>pivot):
        print('2 call', a, l, r)
        qsort(a,pivot+1,r)
a=[4,-2,1,-2,3]
n=len(a)
qsort(a,0,n-1)
print(a)