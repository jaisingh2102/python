# The code below checks if a given number is even or odd. It takes input from the user, converts it to an integer, and then uses the modulus operator to determine if the number is divisible by 2 (even) or not (odd).
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")