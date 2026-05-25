# Simple Calculator
a = float(input("enter first number:"))
b = float(input("enter second number:"))
number = float(input("""enter your choice:
\n1.addition 
\n2.subtraction 
\n3.multiplication
\n4.dividsion 
\n5.exponent 
\n6.floor dividion\n\n"""))
print("you have entered",number)
add = a+b
sub = a-b
mul = a*b
div = a/b
floor_div = a//b
exp = a**b

if number == 1:
    print("addition of two number is",add)
elif number == 2:
    print("subtraction of two number is",sub)
elif number == 3:
    print("multiplication of two number is",mul)
elif number == 4:
    print("division of two number is",div)
elif number == 5:
    print("exponent of two number is",exp)
elif number == 6:
    print("floor division of two number is",floor_div)

else:
    print("invalid choice")