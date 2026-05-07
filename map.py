nums = ["10", "20", "30", "40"]

result = list(map(int, nums))# The 'map' function is used to apply the 'int' function to each element in the 'nums' list, converting the string representations of numbers into actual integers. The result is a map object that can be converted into a list or iterated over to access the converted values. In this case, we convert it directly into a list.

print("Integers:", result)