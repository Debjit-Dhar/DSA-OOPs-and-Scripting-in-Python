n=int(input('Enter the no. of unknowns.'))
print('Enter the augumented matrix')
i,j,k=0,0,0
a = [[0 for i in range(n+1)] for j in range(n)]
for i in range(n):
    for j in range(n+1):
        a[i][j]=float(input('Enter'))
print(a)
for k in range(n):
    for j in range(k+1,n):
        if a[k][k]==0:
            continue
        u=a[j][k]/a[k][k]
        for i in range(k,n+1):
            a[j][i]-=u*a[k][i]
print(a)
x=[0 for i in range(n+1)]
x[3]=a[n-1][n]/a[n-1][n-1]
for i in range(n-2,-1,-1):
    u=a[i][n]
    for j in range(n-1,i,-1):
        u-=a[i][j]*x[j+1]
    x[i+1]=u/a[i][j-1]
print(x)
