+716
Lines changed: 716 additions & 0 deletions
Original file line number	Diff line number	Diff line change
@@ -0,0 +1,716 @@
l=int(input("length in cm"))
b=int(input("breadth in cm"))
a=l*b
print("your area rectangle is:",a,"cm^")
o/p :length in cm 4
breadth in cm 8
your area rectangle is: 32 cm^
r=int(input("enter your radious"))
a=5.16*(r*r)
print("your area is:",a)
o/p:enter your radious 25
your area is: 3225.0
l=int(input("enter length"))
b=int(input("enter breadth"))
h=int(input("enter height"))
a=2*(1*b+b*h+h*1)
print("the area is:",a)
o/p:enter length 8
enter breadth 5
enter height 10
the area is: 130
r=int(input("enter radious"))
h=int(input("enter height"))
a=2*(3.14*(r*h))
print("your c.s.a is:",a)
o/p:enter radious 10
enter height 30
your c.s.a is: 10980.0
r=int(input("enter radious"))
h=int(input("enter height"))
a=2.3.14*r*(r+h)
print("area is:",a)
o/p:enter radious 8
enter height 10
area is: 3654.7200000000003
r=int(input("enter radious"))
l=int(input("enter length"))
a=3.14*r*l
print("csa is:",a)
o/p:enter radious 11
enter length 26
csa is: 49.61
r=int(input("enter radious"))
l=int(input("enter slant height8"))
a=3.14*r*(1+r)
print("the tsa is:",a)
o/p:enter radious 15
enter slant height8 32
the tsa is: 753.6
a=int(input("enter length of cube"))
x=6*(a*a)
print("the area of cube is:",x)
o/p:enter length of cube 4
the area of cube is: 96
r=int(input("enter radious"))
a=4*(3.14*(r*r))
print("tsa of sphere is:",a)o/p:
o/p:enter radious 16
tsa of sphere is: 3215.36
l=int(input("enter length"))
b=int(input("enter breadth"))
h=int(input("enter height"))
a=l*b*h
print("volume of cubiodis:",a)
o/p:enter length 18
enter breadth 15
enter height 16
volume of cubiodis: 4320
l=int(input("enter length"))
a=l*l*l
print("volume ofcube is:",a)
o/p:enter length 22
volume ofcube is: 10648
r=int(input("enter radious"))
h=int(input("enter height"))
v=3.14*(r*r)*h
print("volume is:",v)
o/p:enter radious 32
enter height 45
volume is: 48230.4
r=int(input("enter radious"))
v=4/3*(3.14*(r*r*r))
print("volume is:",v)
o/p:enter radious 23
volume is: 50939.17333333334
l=int(input("enter length in cm"))
b=int(input("enter breadth in cm"))
a=2*(l+b)
print("perimeter of rectangle is:",a,"cm")
o/p:enter length in cm 4
enter breadth in cm 6
perimeter of rectangle is: 20 cm
a=int(input("enter length in cm"))
x=a*a
print("your area of square is:",x,"cm^2")
o/p:enter length in cm 42
your area of square is: 1764 cm^2
h=int(input("enter height"))
b=int(input("enter base"))
a=1/2*(b*h)
print("your area is:",a,"cm^2")
o/p:enter height 5
enter base 12
your area is: 30.0 cm^2
a=int(input("enter frist no"))
b=int(input("enter second no"))
c=int(input("enter third no"))
if a>b:
    if a>c:
        print("the greatest no is:",a)
    else:
        print("the greatest no is:",c)
else:
    if b>c:
        print("the greatest no is:",b)
    else:
        print("the greatest no is:",c)
o/p:enter frist no 12
enter second no 10
enter third no 15
the greatest no is: 15
a=int(input("enter frist side of tringle"))
b=int(input("enter second side of tringle"))
c=int(input("enter third side of tringle"))
perimeter=a+b+c
print("the perimeter is:",perimeter)
o/p:enter frist side of tringle 6
enter second side of tringle 4
enter third side of tringle 8
the perimeter is: 18
a=float(input("enter frist no"))
b=float(input("enter second no"))
c=float(input("enter third no"))
d=float(input("enter fourth no"))
if (a>b and a>c and a>d):
    print("greatest number is:",a)
elif (b>c and b>d):
     print("greatest number is:",b)
elif (c>d):
     print("greatest number is:",c)
elif (d>c):
     print("greatest number is:",d)
else:
    print("either any two values or all the four values are equal")