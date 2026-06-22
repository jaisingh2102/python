# list using recursion
gods = ["rama","krishna","shiva","vishnu","hanuman","ganesha"]
def print_list(gods):
    if len(gods) == 0:
        return
    else:
        print(gods[0])
        print_list(gods[1:])


output = print_list(gods)
print(output)        