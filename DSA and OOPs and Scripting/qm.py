def bin(n):
    if(n==0):
        return 0;
    else:
        return bin(n//2)*10+n%2
def check(s1,s2):
    s3=[''for i in range(4)]
    c=0
    for i in range(4):
        if s1[i]==s2[i]:
            s3[i]=list(s1[i])
        else:
            if s1[i]=='-' or s2[i]=='-':
                return ''
            else:
                s3[i]='-'
                c+=1
    if(c==1):
        return str(s3)
    else:
        return ''
L=[0,1,3,7,8,9,11,15]
i,max=0,bin(L[len(L)-1])
b=['' for i in range(len(L))]
for i in range(len(L)):
    n=bin(L[i])
    n=('0'*(len(str(max))-len(str(n)))+str(n))
    b[i]=n
l=[['' for i in range(len(L))]for j in range(5)]
l1=[['' for i in range(len(L))]for j in range(5)]
a0,a1,a2,a3=0,0,0,0
for i in range(len(L)):
    if (L[i] == 0):
        l[0][0] = b[0]
        l1[0][0]=str(L[0])
    elif('1248'.find(str(L[i]))!=-1):
        l[1][a1]=b[i]
        l1[1][a1]=str(L[i])
        a1+=1
    elif('3569'.find(str(L[i]))!=-1 or L[i]==10 or L[i]==12):
        l[2][a2]=b[i]
        l1[2][a3]=str(L[i])
        a2+=1
    elif(L[i]==7 or L[i]==11 or L[i]==13 or L[i]==14):
        l[3][a3]=b[i]
        l1[3][a3]=str(L[i])
        a3+=1
    else:
        l[4][0]=b[i]
        l1[4][0]=L[i]
print(b)
print(l)
print(l1)
s1,s2='',''
for k in range(4):
    for i in range(len(L)):
        if(l[k][i]!=''):
            s1=l[k][i]
            for j in range(len(L)):
                if(l[k+1][i]!=' '):
                    s2=l[k+1][i]
                '''if len(check(s1,s2))!=0:
                    l[k][i+j]=check(s1,s2)
                    l1[k][i+j]=l1[k][i]+','+l1[k][j]'''
                print(s1,s2)
print(l)
print(l1)
