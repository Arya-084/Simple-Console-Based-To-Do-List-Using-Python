
#Console type code for To-Do list.
class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False
    def mark_completed(self):
        self.completed = True
tasks = []
def print_task():
       print("Your Task: ")
       count = 1
       for task in tasks:
            if task.completed:
                status = "Completed"
            else:
                status = "Pending"
            print(count,".",task.description,"-->",status)
            count = count + 1
def is_empty():
    if len(tasks) == 0:
        return True
    else:
        return False 
def add_task():
    description = input("Enter your task description: ")
    task = Task(description)
    tasks.append(task)
    print("Task Added Successfully! ")
def view_task():
    if is_empty():
        print("No Task Available")
    else:
        print_task()
            print(count,".",task.description,"-->",status)
            count = count + 1
def mark_task_completed():
    if is_empty():
        print("No Task Available ")
    else:
        print_task()
        num = int(input("Enter the Task Number: "))
        if num >= 1 and num <= len(tasks):
            tasks[num - 1].mark_completed()
            print("Task Marked As Completed!")
        else:
            print("Invalid Task Number")
while True:
    print("**** To-Do List Menu ****")
    print("1. Add Task")
    print("2. View Task")
    print("3. Marked Task as Complete")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_task()
    elif choice == "2":
        view_task()
    elif choice == "3":
        mark_task_completed()
    elif choice == "4":
        print("Exiting Application....")
        break
    else:
        print("Invalid Choice Input Given")
        pass
