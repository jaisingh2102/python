# This code demonstrates inheritance in Python. The 'car' class inherits from the 'vehicle' class, allowing it to use the 'start' method defined in the 'vehicle' class while also having its own method 'drive'.
class vehicle:
    def start(self):# This method is defined in the 'vehicle' class and can be used by any class that inherits from it.
        print("vehicle is starting")

class car(vehicle):# The 'car' class inherits from the 'vehicle' class, meaning it can use the methods defined in 'vehicle' as well as its own methods.
    def drive(self):
        print("car is driving")

c = car()
c.start()
c.drive()                