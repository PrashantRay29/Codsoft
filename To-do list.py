def print_tasks(tasks):
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def add_task(tasks):
    task = input("Enter a task: ")
    tasks.append(task)
    print(f"Task '{task}' added!")

def remove_task(tasks):
    task_number = int(input("Enter the task number to remove:"))
    try:
        task = tasks.pop(task_number - 1)
        print(f"Task '{task}' removed!")
    except IndexError:
        print("Invalid task number!")

def update_task(tasks):
    task_number = int(input("Enter the task number to update: "))
    try:
        task = tasks[task_number - 1]
        new_task = input(f"Enter the new task (was '{task}'): ")
        tasks[task_number - 1] = new_task
        print(f"Task '{task}' updated to '{new_task}'!")
    except IndexError:
        print("Invalid task number!")

def main():
    tasks = []

    while True:
        print("\nTo-Do List Management System")
        print("1. Add task")
        print("2. Print task")
        print("3. Update task")
        print("4. Remove tasks")
        print("5. Quit")

        choice = input("Choose an option:")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            print_tasks(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            remove_task(tasks)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again!")

if __name__ == "__main__":
    main()
