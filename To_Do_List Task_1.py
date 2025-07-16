import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("📝 To-Do List App")
        self.root.geometry("400x450")
        self.root.config(bg="#F0E68C")

        self.tasks = []

        # Title
        tk.Label(root, text="My To-Do List", font=("Arial", 18, "bold"), bg="#F0E68C").pack(pady=10)

        # Task entry field
        self.task_entry = tk.Entry(root, font=("Arial", 14), width=25)
        self.task_entry.pack(pady=10)

        # Add Task Button
        tk.Button(root, text="Add Task", font=("Arial", 12), command=self.add_task).pack(pady=5)

        # Task list display
        self.task_listbox = tk.Listbox(root, font=("Arial", 14), width=30, height=10, selectbackground="lightblue")
        self.task_listbox.pack(pady=10)

        # Delete Task Button
        tk.Button(root, text="Delete Selected Task", font=("Arial", 12), command=self.delete_task).pack(pady=5)

        # Exit Button
        tk.Button(root, text="Exit", font=("Arial", 12), bg="red", fg="white", command=root.quit).pack(pady=10)

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def delete_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            task_index = selected[0]
            task = self.tasks.pop(task_index)
            self.task_listbox.delete(task_index)
            messagebox.showinfo("Task Deleted", f"Deleted: {task}")
        else:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")

# Create and run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
