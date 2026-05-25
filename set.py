#set:- set is a collection of unordered, unique items.
#It is mutable, meaning you can add or remove items from it. 

collection = {"apple","banana","mango","grapse","papaya",1,2,1,2,3,4}
print(collection) #prints the whole set
print(type(collection)) #prints the type of the collection
#set methods........
#Adding an item to the set
print(len(collection)) #prints the length of the set
collection.add("orange") #adds "orange" to the set
print(collection) #prints the updated set
a = {}
print(type(a)) #prints the type of a, which is dict
b = set()
print(type(b)) #prints the type of b, which is set
collection.remove("banana") #removes "banana" from the set
collection.remove(1) #removes 1 from the set
print(collection) #prints the updated set after removing "banana" and 1
collection.clear() #clears all items from the set
print(collection) #prints the empty set
collection1 = {"apple","banana","mango"}
collection1.pop() #removes and returns an arbitrary item from the set
print(collection1) #prints the updated set after popping an item
collection1.pop() #removes and returns an arbitrary item from the set
print(collection1) #prints the updated set after popping an item