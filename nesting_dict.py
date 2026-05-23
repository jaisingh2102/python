# A nested dictionary is a dictionary that contains another dictionary as a value. It allows you to store and organize data in a hierarchical structure. In a nested dictionary, you can have multiple levels of dictionaries, where each level can contain its own set of key-value pairs.
dict = {
    "person1" : {
        "name" : "aman",
        "age" : 20,
        "city" : "lucknow",
        "cgpa" : 7.52
    },
    "person2" :
    {
        "name" : "ayush",
        "age" : 22,
        "city" : "delhi",
        "cgpa" : 8.1

    }
}
print(dict)
print(dict["person1"])
print(dict["person1"]["name"])
print(dict["person2"]["cgpa"])
print(dict["person2"])