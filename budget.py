import pandas as pd
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import os

# Global variables
users = {}  # To store username-password pairs
current_user = None  # Track the currently logged-in user
data_files_dir = "user_data"  # Directory to save individual user files

# Ensure directory for user files exists
if not os.path.exists(data_files_dir):
    os.makedirs(data_files_dir)

def save_user_data():
    """Save user credentials to a file."""
    with open("users.txt", "w") as file:
        for username, password in users.items():
            file.write(f"{username}:{password}\n")

def load_user_data():
    """Load user credentials from a file."""
    global users
    if os.path.exists("users.txt"):
        with open("users.txt", "r") as file:
            for line in file:
                username, password = line.strip().split(":")
                users[username] = password

def save_budget_data(user):
    """Save budget data for the current user."""
    file_path = os.path.join(data_files_dir, f"{user}_budget.csv")
    budget_data.to_csv(file_path, index=False)

def load_budget_data(user):
    """Load budget data for the current user."""
    global budget_data
    file_path = os.path.join(data_files_dir, f"{user}_budget.csv")
    if os.path.exists(file_path):
        budget_data = pd.read_csv(file_path)
    else:
        budget_data = pd.DataFrame(columns=["Date", "Description", "Category", "Amount"])

# Load user credentials at the start
load_user_data()

# Initialize an empty DataFrame for budget data
budget_data = pd.DataFrame(columns=["Date", "Description", "Category", "Amount"])

# Tkinter GUI
root = tk.Tk()
root.title("Budget App")

# Set background color for a bank-related theme
root.configure(bg="#f5f5dc")  # Beige color to evoke a professional banking theme

def login():
    """Handle user login."""
    global current_user
    username = username_entry.get()
    password = password_entry.get()
    if username in users and users[username] == password:
        current_user = username
        load_budget_data(current_user)
        messagebox.showinfo("Login Successful", f"Welcome, {username}!")
        switch_to_main_screen()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

def register():
    """Handle user registration."""
    username = username_entry.get()
    password = password_entry.get()
    if username in users:
        messagebox.showerror("Registration Failed", "Username already exists.")
    else:
        users[username] = password
        save_user_data()
        messagebox.showinfo("Registration Successful", "User registered successfully!")

def add_transaction_gui():
    """Add transaction via GUI."""
    date = date_entry.get()
    description = desc_entry.get()
    category = category_entry.get()
    try:
        amount = float(amount_entry.get())
        new_transaction = pd.DataFrame([[date, description, category, amount]], columns=["Date", "Description", "Category", "Amount"])
        global budget_data
        budget_data = pd.concat([budget_data, new_transaction], ignore_index=True)
        save_budget_data(current_user)
        messagebox.showinfo("Success", "Transaction added successfully!")
        view_transactions()
    except ValueError:
        messagebox.showerror("Error", "Invalid amount entered.")

def view_transactions():
    """View all transactions."""
    for item in transaction_tree.get_children():
        transaction_tree.delete(item)
    for _, row in budget_data.iterrows():
        transaction_tree.insert("", "end", values=list(row))

def switch_to_main_screen():
    """Switch to the main budget screen."""
    login_frame.pack_forget()
    main_frame.pack()

# Login Frame
login_frame = tk.Frame(root, bg="#f5f5dc", padx=20, pady=20)  # Add padding for better spacing
login_frame.pack()

tk.Label(login_frame, text="Username:", font=("Arial", 14), bg="#f5f5dc").grid(row=0, column=0, pady=10, sticky="e")
username_entry = tk.Entry(login_frame, font=("Arial", 14), width=20)
username_entry.grid(row=0, column=1, pady=10)

tk.Label(login_frame, text="Password:", font=("Arial", 14), bg="#f5f5dc").grid(row=1, column=0, pady=10, sticky="e")
password_entry = tk.Entry(login_frame, font=("Arial", 14), width=20, show="*")
password_entry.grid(row=1, column=1, pady=10)

tk.Button(login_frame, text="Login", font=("Arial", 14), command=login, bg="#4CAF50", fg="white", width=12).grid(row=2, column=0, pady=10)
tk.Button(login_frame, text="Register", font=("Arial", 14), command=register, bg="#4CAF50", fg="white", width=12).grid(row=2, column=1, pady=10)

# Main Frame
main_frame = tk.Frame(root, bg="#f5f5dc")

tk.Label(main_frame, text="Date (YYYY-MM-DD):", font=("Arial", 14), bg="#f5f5dc").grid(row=0, column=0, pady=5)
date_entry = tk.Entry(main_frame, font=("Arial", 14), width=20)
date_entry.grid(row=0, column=1, pady=5)

tk.Label(main_frame, text="Description:", font=("Arial", 14), bg="#f5f5dc").grid(row=1, column=0, pady=5)
desc_entry = tk.Entry(main_frame, font=("Arial", 14), width=20)
desc_entry.grid(row=1, column=1, pady=5)

tk.Label(main_frame, text="Category:", font=("Arial", 14), bg="#f5f5dc").grid(row=2, column=0, pady=5)
category_entry = tk.Entry(main_frame, font=("Arial", 14), width=20)
category_entry.grid(row=2, column=1, pady=5)

tk.Label(main_frame, text="Amount:", font=("Arial", 14), bg="#f5f5dc").grid(row=3, column=0, pady=5)
amount_entry = tk.Entry(main_frame, font=("Arial", 14), width=20)
amount_entry.grid(row=3, column=1, pady=5)

tk.Button(main_frame, text="Add Transaction", font=("Arial", 14), command=add_transaction_gui, bg="#4CAF50", fg="white", width=20).grid(row=4, columnspan=2, pady=10)
tk.Button(main_frame, text="View Transactions", font=("Arial", 14), command=view_transactions, bg="#4CAF50", fg="white", width=20).grid(row=5, columnspan=2, pady=10)

# Transaction Treeview
transaction_tree = ttk.Treeview(main_frame, columns=("Date", "Description", "Category", "Amount"), show="headings", height=10)
transaction_tree.heading("Date", text="Date")
transaction_tree.heading("Description", text="Description")
transaction_tree.heading("Category", text="Category")
transaction_tree.heading("Amount", text="Amount")
transaction_tree.grid(row=6, columnspan=2, pady=10)

# Start the app
root.mainloop()
