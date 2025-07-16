import random
import sqlite3
from tkinter import *
from tkinter import messagebox

# ---------------- SETUP DATABASE ----------------
def setup_database():
    db = sqlite3.connect("users.db")
    cursor = db.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            Username TEXT NOT NULL UNIQUE,
            GeneratedPassword TEXT NOT NULL
        )
    """)
    db.commit()
    db.close()

# --------------- MAIN APP CLASS ----------------
class PasswordApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Password Generator")
        self.root.geometry("500x400")
        self.root.config(bg="#FFB347")

        # Tkinter variables to store input/output
        self.username = StringVar()
        self.password_length = IntVar()
        self.generated_password = StringVar()

        # --- UI Widgets ---
        Label(root, text="Password Generator", font=("Arial", 20, "bold"), bg="#FFB347").pack(pady=20)

        Label(root, text="Enter your name:", font=("Arial", 14), bg="#FFB347").pack()
        Entry(root, textvariable=self.username, font=("Arial", 14)).pack(pady=5)

        Label(root, text="Enter password length:", font=("Arial", 14), bg="#FFB347").pack()
        Entry(root, textvariable=self.password_length, font=("Arial", 14)).pack(pady=5)

        Button(root, text="Generate Password", font=("Arial", 12), command=self.generate_password).pack(pady=10)

        Label(root, text="Your Password:", font=("Arial", 14), bg="#FFB347").pack()
        Entry(root, textvariable=self.generated_password, font=("Arial", 14), fg="red").pack(pady=5)

        Button(root, text="Save to Database", font=("Arial", 12), command=self.save_password).pack(pady=10)
        Button(root, text="Reset", font=("Arial", 12), command=self.reset_fields).pack()

    # ------ Generate Password Logic ------
    def generate_password(self):
        name = self.username.get()
        length = self.password_length.get()

        if not name:
            messagebox.showerror("Error", "Name cannot be empty!")
            return
        if not name.isalpha():
            messagebox.showerror("Error", "Name must contain only letters!")
            return
        if length < 6:
            messagebox.showerror("Error", "Password must be at least 6 characters.")
            return

        characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#&$"
        password = "".join(random.sample(characters, length))
        self.generated_password.set(password)

    # ------ Save to SQLite Database ------
    def save_password(self):
        name = self.username.get()
        password = self.generated_password.get()

        if not password:
            messagebox.showerror("Error", "No password to save.")
            return

        db = sqlite3.connect("users.db")
        cursor = db.cursor()
        try:
            cursor.execute("INSERT INTO users (Username, GeneratedPassword) VALUES (?, ?)", (name, password))
            db.commit()
            messagebox.showinfo("Success", "Password saved successfully!")
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Username already exists.")
        finally:
            db.close()

    # ------ Reset all input fields ------
    def reset_fields(self):
        self.username.set("")
        self.password_length.set(0)
        self.generated_password.set("")

# -------- Run the App --------
if __name__ == "__main__":
    setup_database()
    root = Tk()
    app = PasswordApp(root)
    root.mainloop()
