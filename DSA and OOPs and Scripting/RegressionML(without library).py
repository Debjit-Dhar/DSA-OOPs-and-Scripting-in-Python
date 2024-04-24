import math

n = int(input('Enter the size of the training set: '))

train_x = [0 for _ in range(n+1)]
train_y = [0 for _ in range(n+1)]

# Collect training set data
for i in range(n):
    train_x[i] = float(input('Enter xi: '))
    train_y[i] = float(input('Enter yi: '))

print("Training set x: ", train_x)
print("Training set y: ", train_y)

N = 2
a = [[0.0 for _ in range(N + 2)] for _ in range(N + 1)]
a[0][0] = n
for i in range(N+1):
    for j in range(1,N+1):
        for k in range(1,n+1):
            a[i][j]+=math.pow(train_x[k],j+i)
for i in range(1,N+1):
    a[i][0]=0
    for k in range(1,n+1):
        a[i][0]+=math.pow(train_x[k],i)
for i in range(N+1):
    a[i][N+1]=0
    for k in range(1,n+1):
        a[i][N+1]+=train_y[k]*math.pow(train_x[k],i)
for i in range(0,N+1):
    for j in range(0,N+2):
        print(a[i][j])
    print("\n")
n=N+1
#TRIANGULIZE
for k in range(0,n):
    for j in range(k+1,n):
        u=a[j][k]/a[k][k]
        for i in range(k,n+1):
            a[j][i]=a[j][i]-u*a[k][i]

for i in range(0,n):
    for j in range(0,n+1):
        print(a[i][j])
    print("\n")
flag=0
for j in range(0,n):
    if(a[n-1][j]!=0):
        flag=1
        break
if(flag==0):
    if(a[n-1][n]==0):
        print("Infinite many solutions.")
        exit(1)
    else:
        print("No solutions.")
        exit(1)
#BACK SUBSTITUTE
X=[0 for i in range(n+1)]
X[n]=a[n-1][n]/a[n-1][n-1]
for i in range (n-2,-1,-1):
    u=a[i][n]
    for j in range (n-1,i,-1):
        u-=a[i][j]*X[j+1]
    X[i+1]=u/a[i][j]
l=int(input('Enter size of testing set'))
test_x=[0 for _ in range(l)]
test_y=[0 for _ in range(l)]
per=[0 for _ in range(l)]
print("Polynomial of Regression of degree", N, "is y =", end=' ')
for i in range(1, n + 1):
    if(X[i]>0):
        print(" +", X[i], "x^", i - 1, end=' ')
    else:
        print(" ", X[i], "x^", i - 1, end=' ')
print()
for i in range(l):
    test_x[i]=float(input('Enter xi'))
    test_y[i]=float(input('Enter yi'))
for i in range(l):
    for j in range(1,n+1):
        per[i]+=X[j]*math.pow(test_x[i],j-1)
    per[i]=math.fabs(test_y[i]-per[i])/test_y[i]
avg=0
for i in range(l):
    avg+=per[i]
print("Average Accuracy= ",100-(avg/l)*100,"%")

print()

