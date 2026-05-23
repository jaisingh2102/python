# The code below takes a number as input from the user and prints the multiplication table for that number from 1 to 10. It uses a for loop to iterate through the numbers 1 to 10, and in each iteration, it calculates the product of the input number 'a' and the current number 'i', and then prints the result in a formatted string.
a = int(input("enter a number: "))
for i in range(1,11):
    print(a,"*",i,"=",a*i)