# Average Calculator by 3 numbers
def calc_avg(a,b,c):
    avg = (a+b+c)/3
    return avg

a = int(input("enter first number: "))
b = int(input("enter second number: "))
c = int(input("enter third number: "))
output = calc_avg(a, b, c)
print("the average of", a, b, "and", c, "is", output)