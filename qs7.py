# Create a dictionary to store the marks of different subjects
marks ={}
a = int(input("enter the marks of javascript:"))
marks.update({"javascript": a})
b = int(input("enter the marks of java: "))
marks.update({"java" :b})
c= int(input("enter the marks of python: "))
marks.update({"python" :c})
print(marks)