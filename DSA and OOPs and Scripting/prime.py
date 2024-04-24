def isPrime(n):
    i=2
    for i in range(2,n):
        if n%i==0:
            return 1
        i+=1
    else:
        return 0
n=int(input('Enter number'))
i=2
for i in range(2,n+1):
    if(isPrime(i)==0):
        print(i)
    i+=1

