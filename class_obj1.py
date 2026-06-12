# Define a class called "employee" with attributes such as name, age, salary, and id. Create a list of employee objects and print their details.
class employee:
    def __init__(self,name,age,salary,id):
        self.name = name
        self.age = age
        self.salary = salary
        self.id = id


employees = []

n = int(input("enter the number of employees:"))
for i in range(n):
    name = input("enter the name of employee: ")
    age = int(input("enter the age of the employee:"))
    salary = float(input("enter the salary of the employee:"))
    id = int(input("enter the id of the employee:"))
    emp = employee(name,age,salary,id)
    employees.append(emp)

    print("employee details:")
for emp in employees:
        print("name:",emp.name)
        print("age:",emp.age)
        print("salary:",emp.salary)
        print("id:",emp.id)
