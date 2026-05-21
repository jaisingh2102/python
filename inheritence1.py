# Inheritance in Python allows a new class (called  This promotes code reusability and establishes a natural hierarchical relationship between classes. In this example, we have a base class 'employee' and a derived class 'engineer' that inherits from 'employee'. The 'engineer' class can access the 'work' method from the 'employee' class and also has its own method 'code'.
class employee:# This is the base class 'employee' which has a method 'work'.
    def work(self):
        print("employees are working")a child class or subclass) to inherit attributes and methods from an existing class (called a parent class or base class).


class engineer(employee):# The 'engineer' class inherits from the 'employee' class.
    def code(self):
        print("engineers are doing coding on a project")


e = engineer()# An instance of the 'engineer' class is created, which can access the 'work' method from the 'employee' class and the 'code' method from the 'engineer' class.
e.work()
e.code()                