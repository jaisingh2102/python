class car:
    def __init__(self,name,price,model):
        self.name = name
        self.price = price
        self.model = model

        cars = []

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