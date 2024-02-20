import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")

        # Create a list to store tasks
        self.tasks = []

        # Create a Tkinter StringVar to track the input task
        self.task_var = tk.StringVar()

        # Create and pack the necessary widgets
        self.create_widgets()

    def create_widgets(self):
        # Entry for task input
        entry_task = tk.Entry(self.root, textvariable=self.task_var, width=30)
        entry_task.pack(pady=10)

        # Button to add a task
        add_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        add_button.pack(pady=5)

        # Listbox to display tasks
        self.task_listbox = tk.Listbox(self.root, width=30, selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=10)

        # Button to remove selected task
        remove_button = tk.Button(self.root, text="Remove Task", command=self.remove_task)
        remove_button.pack(pady=5)

    def add_task(self):
        task = self.task_var.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_var.set("")  # Clear the entry after adding task
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def remove_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            self.task_listbox.delete(selected_index)
            self.tasks.pop(selected_index[0])
        else:
            messagebox.showwarning("Warning", "Please select a task to remove.")


if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
