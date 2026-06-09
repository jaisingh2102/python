# Program to calculate age based on birth year and current year, and determine if the person is an adult or a minor.
birth_year = int(input("Enter birth year: "))
current_year = int(input("Enter current year: "))

age = current_year - birth_year
print("Your age is:", age)

if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")