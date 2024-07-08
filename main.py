import json
import os

TODO_FILE = "todo_list.json"


# Load existing tasks from the file
def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            return json.load(file)
    return []


# Save tasks to the file
def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file)


def add_task(tasks, task):
    tasks.append(task)
    save_tasks(tasks)


def view_tasks(tasks):
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")


def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List App - Version 2")
        print("1. View tasks")
        print("2. Add task")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            task = input("Enter a new task: ")
            add_task(tasks, task)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
