'''To-Do List CLI
1. Build a simple to-do app that runs in the terminal.

Features to include:
- Add new tasks (entered by user)
- Show all tasks (with numbering)
- Remove a task by its number or name
- Store tasks in a list while the program is running
- Use functions for: adding, showing, and deleting tasks'''

def add_task(tasks_list):
    task = input("Enter a task: ")
    tasks_list.append(task)

def print_tasks(tasks_list):
    if not tasks_list:
        print("Your to-do list is empty!")
    else:
        print("Your To-do List:")
        for i, task in enumerate(tasks_list, start=1):
            print(f"{i}. {task}")

def remove_task(tasks_list):
    print_tasks(tasks_list)
    if tasks_list:
        try:
            choice = input("Enter task number or name to remove: ")
            if choice.isdigit():  # Remove by number
                index = int(choice) - 1
                if 0 <= index < len(tasks_list):
                    removed = tasks_list.pop(index)
                    print(f"Removed task: {removed}")
                else:
                    print("Invalid number.")
            else:  # Remove by name
                for task in tasks_list:
                    if task.lower() == choice.lower():
                        tasks_list.remove(task)
                        print(f"Removed task: {task}")
                        break
        except:
            print("Error removing task.")

tasks_list = []

print("--- To-do List ---")
print("\nMenu:")
print("1. Add Task")
print("2. Show Tasks")
print("3. Remove Task")
print("4. Quit")

while True:
    
    choice = input("Enter your choice from menu: ")

    if choice == "1":
        add_task(tasks_list)
    elif choice == "2":
        print_tasks(tasks_list)
    elif choice == "3":
        remove_task(tasks_list)
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Please try again.")
