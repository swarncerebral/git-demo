print("Starting the new Python file")
import tkinter as tk
from tkinter import messagebox

def login():
	username = username_entry.get()
	password = password_entry.get()
	if username and password:
		messagebox.showinfo("Login", f"Welcome, {username}!")
	else:
		messagebox.showwarning("Login Failed", "Please enter both username and password.")

root = tk.Tk()
root.title("Login Page")
root.geometry("300x180")

tk.Label(root, text="Username:").pack(pady=(20, 5))
username_entry = tk.Entry(root)
username_entry.pack(pady=5)

tk.Label(root, text="Password:").pack(pady=5)
password_entry = tk.Entry(root, show="*")
password_entry.pack(pady=5)

login_button = tk.Button(root, text="Login", command=login)
login_button.pack(pady=15)

root.mainloop()