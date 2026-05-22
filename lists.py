# liste:- a build-in data structure that stores multiple elements of different data types in a single variable.

# Lists are defined using square brackets [] and elements are separated by commas.
a = ["aman", 20, 7.52, "codder"]
print(type(a))
print(a)
print(a[3])
print(len(a))
a[3] = "engineer"
print(a)
b = a[ :2]
print(b)
c = a[0 :]
print(c)
d = a[-3:-1]
print(d)