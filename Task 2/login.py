# login.py
import json
import hashlib
from tkinter import *
from tkinter import messagebox


# File to store users
USER_FILE = "users.json"

class loginClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Login - Inventory Management System")
        self.root.geometry("400x400")
        self.root.config(bg="white")

        # Title Label
        Label(self.root, text="Login", font=("Arial", 20, "bold"), bg="white").pack(pady=10)

        # Username Field
        Label(self.root, text="Username:", font=("Arial", 12), bg="white").pack(pady=5)
        self.username_entry = Entry(self.root, font=("Arial", 12), bd=2)
        self.username_entry.pack(pady=5)

        # Password Field
        Label(self.root, text="Password:", font=("Arial", 12), bg="white").pack(pady=5)
        self.password_entry = Entry(self.root, font=("Arial", 12), bd=2, show="*")
        self.password_entry.pack(pady=5)

        # Login Button
        Button(self.root, text="Login", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white",
               command=self.check_login).pack(pady=10)

        # Register Button
        Button(self.root, text="Register", font=("Arial", 12, "bold"), bg="blue", fg="white",
               command=self.register_user).pack(pady=5)

        # Exit Button
        Button(self.root, text="Exit", font=("Arial", 12, "bold"), bg="red", fg="white",
               command=self.root.destroy).pack(pady=5)

    def check_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Load users from file
        users = self.load_users()

        if username in users and users[username] == self.hash_password(password):
            messagebox.showinfo("Login Successful", "Welcome to Inventory Management System!")
            self.root.destroy()  # Close login window after success
        else:
            messagebox.showerror("Login Failed", "Invalid Username or Password")

    def register_user(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not username or not password:
            messagebox.showerror("Error", "Username and Password cannot be empty!")
            return

        users = self.load_users()

        if username in users:
            messagebox.showerror("Error", "Username already exists!")
        else:
            users[username] = self.hash_password(password)
            self.save_users(users)
            messagebox.showinfo("Success", "User Registered Successfully!")

    @staticmethod
    def hash_password(password):
        """Hashes the password using SHA256"""
        return hashlib.sha256(password.encode()).hexdigest()

    @staticmethod
    def load_users():
        """Loads user data from JSON file"""
        try:
            with open(USER_FILE, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    @staticmethod
    def save_users(users):
        """Saves user data to JSON file"""
        with open(USER_FILE, "w") as file:
            json.dump(users, file, indent=4)

if __name__ == "__main__":
    root = Tk()
    obj = loginClass(root)
    root.mainloop()
