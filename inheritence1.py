class employee:# This is the base class 'employee' which has a method 'work'.
    def work(self):
        print("employees are working")


class engineer(employee):# The 'engineer' class inherits from the 'employee' class.
    def code(self):
        print("engineers are doing coding on a project")


e = engineer()# An instance of the 'engineer' class is created, which can access the 'work' method from the 'employee' class and the 'code' method from the 'engineer' class.
e.work()
e.code()                