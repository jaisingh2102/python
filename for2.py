list = [1,4,9,16,25,36,49,64,81,100]
x = int(input("enter a number to search: "))
for i in range(len(list)):
    if  list[i] == x:
        print("number found at index", i)
        break
else:
    print("number not found")