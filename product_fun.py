# The code below defines a function called 'calc_product' that takes two parameters, 'a' and 'b'. It calculates the product of these two numbers and returns the result. The code then prompts the user to enter two numbers, calls the 'calc_product' function with those numbers, and prints the result in a formatted string.
def calc_product(a , b):
    c = a * b
    return c

    
a = int(input("enter first number: "))
b = int(input("enter second number: "))
output = calc_product(a , b)
print("the product of", a, "and", b, "is", output)

