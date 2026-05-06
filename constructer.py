class car:# This is the 'car' class which has an initializer method '__init__' that takes three parameters: 'name', 'price', and 'model'. These parameters are used to initialize the attributes of the 'car' object.
    def __init__(self,name,price,model):# The '__init__' method is a special method in Python that is called when an object is created. It is used to initialize the attributes of the object with the values passed as arguments.
        self.name = name
        self.price = price
        self.model = model

        cars = []# An empty list 'cars' is created to store the instances of the 'car' class that will be created based on user input.

n = int(input("enter the number of cars:"))
for i in range(n):
    name = input("enter the name of the car: ")
    price = float(input("enter the price of the car:"))
    model = input("enter the model of the car:")
    c = car(name,price,model)
    cars.append(c)
    print("car details:")
for c in cars:
        print("name:",c.name)
        print("price:",c.price)
        print("model:",c.model)