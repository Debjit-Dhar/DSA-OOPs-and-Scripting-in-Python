n=int(input('Enter the no. of unknowns.'))
print('Enter the augumented matrix')
i,j,k=0,0,0
a = [[0 for i in range(n+1)] for j in range(n)]
for i in range(n):
    for j in range(n+1):
        a[i][j]=float(input('Enter'))
print(a)
for i in range(0,n):
    j=i
    while(a[i][i]==0 and j<n):
        for k in range(0,n+1):
            f=a[i][k]
            a[i][k]=a[j][k]
            a[j][k]=f
        j=j+1
    f=a[i][i]
    if(a[i][i]!=0):
        for k in range(i,n+1):
            a[i][k]/=f
    for k in range(0,n):
        if(k!=i):
            f=a[k][i]/a[i][i]
            for p in range(i,n+1):
                a[k][p]-=f*a[i][p]
print("Reduced Row Echelon Form")
print(a)
x=[0 for i in range(n+1)]
for i in range(0,n):
    x[i+1]=a[i][n]
print(x)