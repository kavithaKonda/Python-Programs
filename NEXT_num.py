

number=int(input("enter the range"))
frist_value=0
second_value=1
for num in range(0,number):
    if(num<=1):
        NEXT=num
    else:
        NEXT=frist_value+second_value
        frist_value=second_value
        second_value=NEXT
    print(NEXT)