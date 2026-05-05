class animal:
    def eat(self):
        print("animals can eat")

class dog(animal):
    def bark(self):
        print("dogs can bark")


d = dog()
d.eat()        
d.bark()