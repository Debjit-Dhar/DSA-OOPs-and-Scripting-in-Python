file1=open("poem.txt","r")
s=" "
while s:
    s=file1.readline()
    print(s,end=' ')
file1.close()
file1=open("poem.txt","r")
str=file1.read()
print('\n')
print('Size of file= ',len(str),'bytes')
file1.close()