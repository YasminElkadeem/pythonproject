"""
Python To-Do List Application
==============================
Allows users to:
- Add tasks
- View tasks
- Delete tasks
- Save tasks in a file (persistent storage)
"""

import json
import os

TASKS_FILE = "tasks.json"


def load_tasks():
    """Load tasks from the JSON file. Returns an empty list if the file doesn't exist or is invalid."""
    if not os.path.exists(TASKS_FILE):
        return []
    try:
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []


def save_tasks(tasks):
    """Save the list of tasks to the JSON file."""
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2)


def add_task(tasks):
    """Prompt the user for a new task description and append it to the list."""
    description = input("Enter the task description: ").strip()
    if not description:
        print("Task description cannot be empty.")
        return
    tasks.append({"description": description, "done": False})
    save_tasks(tasks)
    print(f"Task '{description}' added successfully.")


def view_tasks(tasks):
    """Display all tasks with their index and status."""
    if not tasks:
        print("No tasks to display.")
        return
    print("\n--- Your To-Do List ---")
    for i, task in enumerate(tasks, start=1):
        status = "[✓]" if task.get("done") else "[ ]"
        print(f"{i}. {status} {task['description']}")
    print("------------------------\n")


def delete_task(tasks):
    """Prompt the user for a task number and remove it from the list."""
    view_tasks(tasks)
    if not tasks:
        return
    try:
        index = int(input("Enter the number of the task to delete: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            save_tasks(tasks)
            print(f"Task '{removed['description']}' deleted successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def show_menu():
    """Display the main menu options."""
    print("\n===== TO-DO LIST =====\n")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")
    print("======================")


def main():
    """Main program loop."""
    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()

