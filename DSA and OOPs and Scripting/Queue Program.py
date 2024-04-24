def enqueue(rear,n):
    L[rear]=n
def dequeue(front):
    print("Popping ", L[front])
def display():
    if(rear==-1):
        print("Queue Empty.")
    else:
        print(L[0:rear+1])
size=3
L=[0]*size
front,rear=0,-1
while True:
    print("1:Push\n2:Pop\n3:Display\n4:Exit\nChoice:")
    ch=int(input('Enter choice '))
    if ch==1:
        num=int(input('Enter number '))
        if (rear == size - 1):
            print("Queue Overflow.")
        else:
            rear+=1
            enqueue(rear,num)
    elif ch==2:
        if (rear == -1):
            print("Queue Underflow.")
        else:
            dequeue(front)
            for i in range(0, rear):
                L[i] = L[i + 1]
            rear-=1
    elif ch==3:
        display()
    else:
        break