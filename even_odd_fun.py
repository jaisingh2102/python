# This program defines a function to determine if a given number is even or odd. The function takes an integer as input and returns "even" if the number is divisible by 2, and "odd" otherwise. The user is prompted to enter a number, and the result is printed to the console.
def calc_even_odd(num):
    if num%2 == 0:
        return "even"
    else:
        return "odd"

a = int(input("enter a number:"))
result = calc_even_odd(a)
print(f"The number {a} is {result}.")
