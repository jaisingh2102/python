#search number x from the given list using while loop
num = [1,4,9,16,25,36,49,64,81,100]
x = int(input("enter a number to search: "))
i = 0
while i<len(num):
    if num[i] == x:
        print("number found at index", i)
        break
    i += 1
else:
    print("number not found")