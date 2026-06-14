#Dictionary is a collection of key value pairs
dict = {
    "name" : "aman",
    "village" : "naikapar",
    "age" : 20,
    "sport" : "cricket",
    "profession" : "computer engineer",
}
print(dict)#prints the whole dictionary
print(dict.keys())#prints the keys of the dictionary
print(dict.values())#prints the values of the dictionary
print(dict.items())#prints the key value pairs of the dictionary
print(dict.get("sport"))#prints the value of the key "sport"
dict.update({"hobby": "coding"})#updates the dictionary with the new key value pair
print(dict)
