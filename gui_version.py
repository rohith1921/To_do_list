import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

# Define the file for saving tasks
TASKS_FILE = "tasks.json"

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.tasks = self.load_tasks()

        self.task_listbox = tk.Listbox(root, height=10, width=50)
        self.task_listbox.pack(pady=10)

        self.add_task_entry = tk.Entry(root, width=50)
        self.add_task_entry.pack(pady=5)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        self.edit_button = tk.Button(root, text="Edit Task", command=self.edit_task)
        self.edit_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(pady=5)

        self.complete_button = tk.Button(root, text="Mark Task as Complete", command=self.mark_task_complete)
        self.complete_button.pack(pady=5)

        self.save_button = tk.Button(root, text="Save Tasks", command=self.save_tasks)
        self.save_button.pack(pady=5)

        self.refresh_task_list()

    # Load tasks from file
    def load_tasks(self):
        if os.path.exists(TASKS_FILE):
            with open(TASKS_FILE, 'r') as file:
                return json.load(file)
        return []

    # Save tasks to file
    def save_tasks(self):
        with open(TASKS_FILE, 'w') as file:
            json.dump(self.tasks, file, indent=4)
        messagebox.showinfo("Save", "Tasks saved successfully!")

    # Update the listbox with current tasks
    def refresh_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for idx, task in enumerate(self.tasks):
            status = "Complete" if task['completed'] else "Incomplete"
            self.task_listbox.insert(tk.END, f"{idx+1}. {task['task']} [{status}]")

    # Add a new task
    def add_task(self):
        task_name = self.add_task_entry.get()
        if task_name:
            self.tasks.append({"task": task_name, "completed": False})
            self.refresh_task_list()
            self.add_task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a task before adding.")

    # Edit a selected task
    def edit_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            selected_task = self.tasks[selected_index[0]]['task']
            new_task_name = simpledialog.askstring("Edit Task", f"Edit the task: {selected_task}")
            if new_task_name:
                self.tasks[selected_index[0]]['task'] = new_task_name
                self.refresh_task_list()
        else:
            messagebox.showwarning("Selection Error", "Please select a task to edit.")

    # Delete a selected task
    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            self.tasks.pop(selected_index[0])
            self.refresh_task_list()
        else:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")

    # Mark a task as complete
    def mark_task_complete(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            self.tasks[selected_index[0]]['completed'] = True
            self.refresh_task_list()
        else:
            messagebox.showwarning("Selection Error", "Please select a task to mark as complete.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
