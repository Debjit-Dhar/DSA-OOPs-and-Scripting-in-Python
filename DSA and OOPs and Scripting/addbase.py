b=int(input('Enter base'))
n1=input('Enter first no.')
n2=input('Enter second no.')
n1,n2=n1[::-1],n2[::-1]
dif=0
if(len(n1)>len(n2)):
    dif=len(n1)-len(n2)
    n2+="0"*dif
else:
    dif=len(n2)-len(n1)
    n1+="0"*dif
i,sum,carry=0,0,0
ans=""
for i in range(max(len(n1),len(n2))):
    if(n1[i].isalpha()):
        d1=ord(n1[i])-55
    else:
        d1=int(n1[i])
    if(n2[i].isalpha()):
        d2=ord(n2[i])-55
    else:
        d2=int(n2[i])
    sum=(d1+d2+carry)%b
    carry=int((d1+d2+carry)/b)
    print(d1,' ',d2,' ',sum,' ',carry)
    if sum>=10:
        sum=chr(sum+55)
    ans+=str(sum)
ans=ans[::-1]
if carry!=0:
    ans=str(carry)+ans
print('done')
print(ans)
