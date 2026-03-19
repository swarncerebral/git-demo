
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
root.title("Attractive Login Page")
root.geometry("350x260")
root.configure(bg="#222831")

# Frame for the login box
login_frame = tk.Frame(root, bg="#393E46", bd=2, relief=tk.RIDGE)
login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER, width=300, height=200)

title_label = tk.Label(login_frame, text="Login", font=("Arial", 18, "bold"), bg="#393E46", fg="#FFD369")
title_label.pack(pady=(15, 10))

tk.Label(login_frame, text="Username", font=("Arial", 11), bg="#393E46", fg="#EEEEEE").pack(pady=(0, 3))
username_entry = tk.Entry(login_frame, font=("Arial", 11), bg="#EEEEEE", fg="#222831", relief=tk.FLAT)
username_entry.pack(ipady=3, pady=(0, 10), padx=20, fill=tk.X)

tk.Label(login_frame, text="Password", font=("Arial", 11), bg="#393E46", fg="#EEEEEE").pack(pady=(0, 3))
password_entry = tk.Entry(login_frame, show="*", font=("Arial", 11), bg="#EEEEEE", fg="#222831", relief=tk.FLAT)
password_entry.pack(ipady=3, pady=(0, 15), padx=20, fill=tk.X)

login_button = tk.Button(login_frame, text="Login", font=("Arial", 11, "bold"), bg="#FFD369", fg="#222831", activebackground="#FFD369", activeforeground="#222831", command=login, relief=tk.FLAT, cursor="hand2")
login_button.pack(pady=(0, 10), ipadx=10, ipady=2)

root.mainloop()