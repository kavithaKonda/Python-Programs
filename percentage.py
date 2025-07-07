a=eval(input("enter marks out of 300"))
b=a/300*100
print("percentage is",b,"%")
if(a>300):
    print("you enter a wrong marks")
elif b>60:
     print("your divison is frist")
elif (b>50 and b<53):
     print("your dividon is second")
elif(b>33 and b<50):
     print("your divison is third")
else:
    print("fail")