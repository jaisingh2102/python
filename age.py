# This program calculates the age of a person based on their birth year and the current year.
birth_year = int(input("Enter birth year: "))
current_year = int(input("Enter current year: "))

age = current_year - birth_year
print("Your age is:", age)

if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")