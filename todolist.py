import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List")

        # Task list
        self.tasks = []

        # Entry for adding tasks
        self.task_entry = tk.Entry(self.master, width=30)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        # Add Task button
        add_button = tk.Button(self.master, text="Add Task", command=self.add_task)
        add_button.grid(row=0, column=1, padx=10, pady=10)

        # Listbox to display tasks
        self.task_listbox = tk.Listbox(self.master, width=50, height=10)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # Remove Task button
        remove_button = tk.Button(self.master, text="Remove Task", command=self.remove_task)
        remove_button.grid(row=2, column=0, padx=10, pady=10)

        # Clear All button
        clear_button = tk.Button(self.master, text="Clear All", command=self.clear_all_tasks)
        clear_button.grid(row=2, column=1, padx=10, pady=10)

        # Populate tasks from the list
        self.update_task_listbox()

    def add_task(self):
        new_task = self.task_entry.get()
        if new_task:
            self.tasks.append(new_task)
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def remove_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            self.tasks.pop(selected_task_index[0])
            self.update_task_listbox()
        else:
            messagebox.showwarning("Warning", "Please select a task to remove.")

    def clear_all_tasks(self):
        self.tasks = []
        self.update_task_listbox()

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)
if __name__ == "__main__":
    root = tk.Tk()
    todo_app = ToDoApp(root)
    root.mainloop()
