import tkinter as tk
from tkinter import messagebox, simpledialog
import mysql.connector


class ATM:
    def __init__(self, master):
        self.master = master
        master.title("ATM Interface")
        master.geometry("400x400")

        # Establish database connection
        try:
            self.conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="AvnishuRootSQL",
                database="atm_db"
            )
            self.cursor = self.conn.cursor(dictionary=True)
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error connecting to database: {err}")
            master.destroy()
            return

        self.current_user = None

        self.label = tk.Label(master, text="Welcome to the ATM", font=("Arial", 16))
        self.label.grid(row=0, column=0, columnspan=2, pady=20)

        self.register_button = tk.Button(master, text="Register", command=self.register)
        self.register_button.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        self.login_button = tk.Button(master, text="Login", command=self.login)
        self.login_button.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

        self.check_balance_button = tk.Button(master, text="Check Balance", command=self.check_balance)
        self.check_balance_button.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

        self.deposit_button = tk.Button(master, text="Deposit Money", command=self.deposit)
        self.deposit_button.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

        self.withdraw_button = tk.Button(master, text="Withdraw Money", command=self.withdraw)
        self.withdraw_button.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

        self.exit_button = tk.Button(master, text="Exit", command=self.close)
        self.exit_button.grid(row=3, column=1, padx=10, pady=10, sticky="ew")


        master.grid_columnconfigure(0, weight=1)
        master.grid_columnconfigure(1, weight=1)

    def register(self):
        username = simpledialog.askstring("Register", "Enter a username:")
        if not username:
            return

        self.cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        if self.cursor.fetchone():
            messagebox.showerror("Error", "Username already exists!")
            return
        password = simpledialog.askstring("Register", "Enter a password:", show='*')
        if not password:
            return
        try:

            self.cursor.execute(
                "INSERT INTO users (username, password, balance) VALUES (%s, %s, %s)",
                (username, password, 0)
            )
            self.conn.commit()
            messagebox.showinfo("Success", "User registered successfully!")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error registering user: {err}")

    def login(self):
        username = simpledialog.askstring("Login", "Enter your username:")
        if not username:
            return
        password = simpledialog.askstring("Login", "Enter your password:", show='*')
        if not password:
            return
        self.cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        result = self.cursor.fetchone()
        if result:
            self.current_user = username
            messagebox.showinfo("Success", f"Welcome, {username}!")
        else:
            messagebox.showerror("Error", "Invalid username or password!")

    def check_balance(self):
        if self.current_user:
            self.cursor.execute("SELECT balance FROM users WHERE username = %s", (self.current_user,))
            result = self.cursor.fetchone()
            if result:
                balance = result['balance']
                messagebox.showinfo("Balance", f"Your balance is: ₹{balance:.2f}")
        else:
            messagebox.showwarning("Warning", "Please log in first!")

    def deposit(self):
        if self.current_user:
            amount = self.get_amount("Enter amount to deposit:")
            if amount is not None:
                try:
                    self.cursor.execute("UPDATE users SET balance = balance + %s WHERE username = %s",
                                        (amount, self.current_user))
                    self.conn.commit()
                    messagebox.showinfo("Deposit", f"You have deposited: ₹{amount:.2f}")
                except mysql.connector.Error as err:
                    messagebox.showerror("Error", f"Error during deposit: {err}")
        else:
            messagebox.showwarning("Warning", "Please log in first!")

    def withdraw(self):
        if self.current_user:
            amount = self.get_amount("Enter amount to withdraw:")
            if amount is not None:
                # Retrieve current balance
                self.cursor.execute("SELECT balance FROM users WHERE username = %s", (self.current_user,))
                result = self.cursor.fetchone()
                if result:
                    balance = result['balance']
                    if amount <= balance:
                        try:
                            self.cursor.execute("UPDATE users SET balance = balance - %s WHERE username = %s",
                                                (amount, self.current_user))
                            self.conn.commit()
                            messagebox.showinfo("Withdraw", f"You have withdrawn: ₹{amount:.2f}")
                        except mysql.connector.Error as err:
                            messagebox.showerror("Error", f"Error during withdrawal: {err}")
                    else:
                        messagebox.showwarning("Withdraw", "Insufficient funds!")
        else:
            messagebox.showwarning("Warning", "Please log in first!")

    def get_amount(self, prompt):
        amount_str = simpledialog.askstring("Input", prompt)
        if amount_str is not None:
            try:
                amount = float(amount_str)
                if amount < 0:
                    raise ValueError("Negative amount")
                return amount
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid amount.")
        return None

    def close(self):

        if self.conn.is_connected():
            self.cursor.close()
            self.conn.close()
        self.master.quit()


if __name__ == "__main__":
    root = tk.Tk()
    atm = ATM(root)
    root.mainloop()
