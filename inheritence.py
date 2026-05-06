class animal:# This is the base class 'animal' which has a method 'eat'.
    def eat(self):
        print("animals can eat")

class dog(animal):# The 'dog' class inherits from the 'animal' class.
    def bark(self):
        print("dogs can bark")


d = dog()# An instance of the 'dog' class is created, which can access the 'eat' method from the 'animal' class and the 'bark' method from the 'dog' class.
d.eat()        
d.bark()