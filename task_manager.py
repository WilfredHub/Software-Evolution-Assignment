tasks = []

def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    print("Task added.")

def view_tasks():
    for task in tasks:
        print(task)

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Exit") 

    choice = input("Choose option: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        break
