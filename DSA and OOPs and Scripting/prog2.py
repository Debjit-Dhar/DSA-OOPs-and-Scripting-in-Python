y=int(input('Enter year '))
if y%400==0:
    print("Leap")
elif y%4==0 and y%100!=0:
    print("Leap")
else:
    print("Not Leap")