import os
import json

# Define the file where tasks will be saved
TASKS_FILE = "tasks.json"

# Load tasks from file if it exists
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

# Display tasks with their status
def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    print("\nCurrent Tasks:")
    for idx, task in enumerate(tasks, start=1):
        status = "Complete" if task['completed'] else "Incomplete"
        print(f"{idx}. {task['task']} [{status}]")

# Add a new task
def add_task(tasks):
    task_name = input("Enter the new task: ")
    tasks.append({"task": task_name, "completed": False})
    print(f"Task '{task_name}' added successfully.")

# Edit an existing task
def edit_task(tasks):
    display_tasks(tasks)
    task_num = int(input("\nEnter the task number to edit: ")) - 1
    if 0 <= task_num < len(tasks):
        new_task_name = input("Enter the new task description: ")
        tasks[task_num]['task'] = new_task_name
        print("Task updated successfully.")
    else:
        print("Invalid task number.")

# Delete a task
def delete_task(tasks):
    display_tasks(tasks)
    task_num = int(input("\nEnter the task number to delete: ")) - 1
    if 0 <= task_num < len(tasks):
        removed_task = tasks.pop(task_num)
        print(f"Task '{removed_task['task']}' deleted successfully.")
    else:
        print("Invalid task number.")

# Mark a task as complete
def mark_task_complete(tasks):
    display_tasks(tasks)
    task_num = int(input("\nEnter the task number to mark as complete: ")) - 1
    if 0 <= task_num < len(tasks):
        tasks[task_num]['completed'] = True
        print(f"Task '{tasks[task_num]['task']}' marked as complete.")
    else:
        print("Invalid task number.")

# Main loop to interact with the user
def main():
    tasks = load_tasks()

    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Display tasks")
        print("2. Add task")
        print("3. Edit task")
        print("4. Delete task")
        print("5. Mark task as complete")
        print("6. Save and exit")

        choice = input("Choose an option (1-6): ")

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            edit_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            mark_task_complete(tasks)
        elif choice == '6':
            save_tasks(tasks)
            print("Tasks saved. Exiting.")
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
