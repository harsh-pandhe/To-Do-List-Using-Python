def add_task(tasks, task):
    tasks.append(task)


def view_tasks(tasks):
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")


def main():
    tasks = []

    while True:
        print("\nTo-Do List App - Version 1")
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
