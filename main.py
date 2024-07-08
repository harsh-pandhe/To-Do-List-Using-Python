import json
import os

TODO_FILE = "todo_list.json"


def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            return json.load(file)
    return []


def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file)


def add_task(tasks, task):
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)


def view_tasks(tasks):
    for index, task in enumerate(tasks, start=1):
        status = "Done" if task["done"] else "Not Done"
        print(f"{index}. {task['task']} - {status}")


def remove_task(tasks, task_number):
    if 0 < task_number <= len(tasks):
        tasks.pop(task_number - 1)
        save_tasks(tasks)
    else:
        print("Invalid task number.")


def mark_task_done(tasks, task_number):
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]["done"] = True
        save_tasks(tasks)
    else:
        print("Invalid task number.")


def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List App - Version 3")
        print("1. View tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Mark task as done")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            task = input("Enter a new task: ")
            add_task(tasks, task)
        elif choice == "3":
            task_number = int(input("Enter the task number to remove: "))
            remove_task(tasks, task_number)
        elif choice == "4":
            task_number = int(input("Enter the task number to mark as done: "))
            mark_task_done(tasks, task_number)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
