# This code finds the common elements between two lists, arr1 and arr2, and stores them in a new list called common. Finally, it prints the common elements.
arr1 = [1, 2, 3, 4]
arr2 = [3, 4, 5, 6]

common = []

for i in arr1:
    if i in arr2:
        common.append(i)

print("Common elements:", common)