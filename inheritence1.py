class employee:
    def work(self):
        print("employees are working")


class engineer(employee):
    def code(self):
        print("engineers are doing coding on a project")


e = engineer()
e.work()
e.code()                