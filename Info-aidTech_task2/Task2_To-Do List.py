import pickle
import tkinter as tk
from tkinter import messagebox

class Task:
    def __init__(self, title, description, status):
        self.title = title
        self.description = description
        self.status = status

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.tasks = []

        self.task_frame = tk.Frame(root)
        self.task_frame.pack(padx=10, pady=10)

        self.title_label = tk.Label(self.task_frame, text="Title:")
        self.title_label.grid(row=0, column=0, sticky=tk.W)
        self.title_entry = tk.Entry(self.task_frame)
        self.title_entry.grid(row=0, column=1, padx=5, pady=5)

        self.desc_label = tk.Label(self.task_frame, text="Description:")
        self.desc_label.grid(row=1, column=0, sticky=tk.W)
        self.desc_entry = tk.Entry(self.task_frame)
        self.desc_entry.grid(row=1, column=1, padx=5, pady=5)

        self.status_label = tk.Label(self.task_frame, text="Status:")
        self.status_label.grid(row=2, column=0, sticky=tk.W)
        self.status_entry = tk.Entry(self.task_frame)
        self.status_entry.grid(row=2, column=1, padx=5, pady=5)

        self.add_button = tk.Button(self.task_frame, text="Add Task", command=self.add_task)
        self.add_button.grid(row=3, column=0, padx=5, pady=5)

        self.delete_button = tk.Button(self.task_frame, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=3, column=1, padx=5, pady=5)

        self.listbox_frame = tk.Frame(root)
        self.listbox_frame.pack(padx=10, pady=10)

        self.tasks_listbox = tk.Listbox(self.listbox_frame, width=50)
        self.tasks_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        self.scrollbar = tk.Scrollbar(self.listbox_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.tasks_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.tasks_listbox.yview)

        self.load_tasks()

    def add_task(self):
        title = self.title_entry.get()
        description = self.desc_entry.get()
        status = self.status_entry.get()

        if title and description and status:
            task = Task(title, description, status)
            self.tasks.append(task)
            self.tasks_listbox.insert(tk.END, task.title)
            self.clear_entries()
        else:
            messagebox.showerror("Error", "All fields must be filled!")

    def delete_task(self):
        selected_index = self.tasks_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            self.tasks.pop(index)
            self.tasks_listbox.delete(selected_index)
        else:
            messagebox.showerror("Error", "No task selected!")

    def clear_entries(self):
        self.title_entry.delete(0, tk.END)
        self.desc_entry.delete(0, tk.END)
        self.status_entry.delete(0, tk.END)

    def load_tasks(self):
        try:
            with open("tasks.pkl", "rb") as file:
                self.tasks = pickle.load(file)
                for task in self.tasks:
                    self.tasks_listbox.insert(tk.END, task.title)
        except FileNotFoundError:
            messagebox.showinfo("Info Invalid")
    def save_tasks(self):
        with open("tasks.pkl", "wb") as file:
            pickle.dump(self.tasks, file)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
    # Save tasks when the application is closed
    app.save_tasks()
