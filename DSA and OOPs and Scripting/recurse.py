def I(i,n):
    if i>n:
        return
    else:
        J(i,1)
        print()
        I(i+1,n)
def J(i,j):
     if j>i:
         return
     else:
         print('*',end='\t')
         J(i,j+1)
n=eval(input('Enter Number'))
I(1,n)


