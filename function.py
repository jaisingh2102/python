#function to calculate sum of two numbers
def sum(a,b):#function definition with parameters a and b
    s = a+b
    return s

a = int(input("enter first number: "))
b = int(input("enter second number:"))
output = sum(a,b)#function call with arguments a and b, the output will be stored in variable output
print("sum of",a,"and",b,"is",output)
