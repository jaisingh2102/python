# This code demonstrates how to convert a list of names to uppercase using the 'map' function and the 'str.upper' method. The 'map' function applies the 'str.upper' method to each element in the 'names' list, resulting in a new list where all the names are in uppercase. Finally, it prints the resulting list of uppercase names.
names = ["himanshu", "anmol", "prashant", "aman", "jay"]

result = list(map(str.upper, names))

print("Uppercase:", result)