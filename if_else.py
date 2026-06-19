#This program takes the marks of a student as input and assigns a grade based on the following criteria:
a = int(input("enter marks of student: "))
if a>=90:
    print("grade A")
elif (a>=80 and a<90):
    print("grade B")
elif (a>=70 and a<80):
    print("grade C")
else:
    print("grade D")