a=eval(input("enter limit"))
list=[]
for a in range(1,a+1):
    a=eval(input("enter element"))
    list.append(a)
print(list)
l=len(list)
for i in range(1):
    for j in range(0,1-i-1):
        if list[j]>list[j+1]:
            temp=list[j]
            list[j]=list[j+1]
            list[j+1]=temp
print("after sorting the list is")
print(list)