# This code defines a function `calc_length` that calculates and prints the length of a given list. It then creates two lists, `cities` and `subjects`, and calls the `calc_length` function for each list to display their lengths.
cities = ["new york", "dilhi","london","mumbai","paris","sydney"]
subjects =["java","python","c++","javascript","ruby","go"]
def calc_length(list):
    print("the length of the list is", len(list))

calc_length(cities)
calc_length(subjects)