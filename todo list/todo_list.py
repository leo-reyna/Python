# todo_list.py
# LR
# Aug 18 2023  Work in progress.
# To Do List - Basic Python


import os

# Initialize an empty list to store tasks
tasks = []
os.system('cls')


# Function to add a task
def add_task(task):  # where task in parentheses is the action of the user wants to save
    tasks.append(task)  # appending 
    print("Task added to list:", task)


# Function to remove a task    
def remove_task(task):
    tasks.remove(task)  # removing from list
    print("Task removed from list", task)


# Function to display all tasks
def display_tasks():
    if tasks:
        print("Tasks:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")
    else:
        print("No tasks to display.")


# Main loop
while True:
    print("\n-- To-Do List Manager --")
    print("1. Add Task")
    print("2. Display Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter the task: ")
        add_task(task)
    elif choice == "2":
        display_tasks()
    elif choice == "3":
        remove_task(task)
    elif choice == "4":
        print("Exiting the To-Do List Manager. Adios!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
