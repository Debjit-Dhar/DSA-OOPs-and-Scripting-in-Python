#Stack is  based on LIFO(Last In First Out) Principle.
def push(size,n):
    if(top<=size-1):
        L[top]=n
def display(top):
    if(top==-1):
        print("Stack empty.")
    else:
        i=top
        print(L[0:i+1])
def pop(top):
    if(top==-1):
        print("Stack underflow.")
    else:
        print("Popping ",L[top])
size=3
L=[0]*size
top=-1
while True:
    print("1.Push\n2.pop\n3.display\n4.exit\nChoice")
    ch=int(input('Enter choice '))
    if ch==1:
        num=int(input('Enter number '))
        if top<size-1:
            top+=1
            push(size,num)
        else:
            print('Stack Overflow')
    elif ch==2:
        pop(top)
        if top!=-1:
            top-=1
    elif ch==3:
        display(top)
    else:
        break