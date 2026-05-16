# This program finds the greatest of three numbers entered by the user.
a = int(input("enter the first number: "))
b = int(input("enter the second number: "))
c = int(input("enter the third number: "))
if(a>=b and a>=c):
    print(a, "is the greatest number: ",a)
elif (b>a and b>=c):
    print(b, "is the greatest number: ",b)
else:
    print("c is the greatest number: ",c)