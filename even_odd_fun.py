# This function checks if a number is even or odd and returns the result as a string.
def calc_even_odd(num):
    if num%2 == 0:
        return "even"
    else:
        return "odd"

a = int(input("enter a number:"))
result = calc_even_odd(a)
print(f"The number {a} is {result}.")
