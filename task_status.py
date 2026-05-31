# This program allows the user to input a task and its completion status, then displays whether the task is completed or pending.
task = input("Enter your task: ")
status = input("Completed? (yes/no): ")

if status == "yes":
    print("Task completed ✅")
else:
    print("Task pending ❌")