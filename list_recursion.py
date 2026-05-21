# This code defines a function 'print_list' that takes a list of 'gods' as input and prints each god's name recursively. The function checks if the list is empty; if it is, it returns. Otherwise, it prints the first element of the list and then calls itself with the rest of the list (excluding the first element). Finally, it calls the function with a predefined list of gods and prints the output.
gods = ["rama","krishna","shiva","vishnu","hanuman","ganesha"]
def print_list(gods):
    if len(gods) == 0:
        return
    else:
        print(gods[0])
        print_list(gods[1:])


output = print_list(gods)
print(output)        