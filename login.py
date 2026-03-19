
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import tkinter.ttk as ttk
from styles import setup_styles

def login():
    username = username_entry.get()
    password = password_entry.get()
    if username and password:
        messagebox.showinfo("Login", f"Welcome, {username}!")
    else:
        messagebox.showwarning("Login Failed", "Please enter both username and password.")

def cancel():
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)



root = tk.Tk()
root.title("Pharma Industry Login")
root.geometry("500x420")  # Increased window size
root.configure(bg="#e3f6f5")
setup_styles()



# Frame for the login box
login_frame = ttk.Frame(root, style='Pharma.TFrame')
login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER, width=420, height=320)  # Increased frame size

# Pharma logo
logo_path = os.path.join(os.path.dirname(__file__), "pharma_logo.png")
if os.path.exists(logo_path):
    logo_img = Image.open(logo_path)
    # Use LANCZOS for resampling in Pillow >= 10.0
    try:
        logo_img = logo_img.resize((60, 60), Image.Resampling.LANCZOS)
    except AttributeError:
        logo_img = logo_img.resize((60, 60), Image.LANCZOS)
    logo_photo = ImageTk.PhotoImage(logo_img)
    logo_label = ttk.Label(login_frame, image=logo_photo, style='Pharma.TLabel')
    logo_label.image = logo_photo
    logo_label.pack(pady=(15, 5))
else:
    logo_label = ttk.Label(login_frame, text="💊", font=("Arial", 32), style='Pharma.TLabel')
    logo_label.pack(pady=(15, 5))


title_label = ttk.Label(login_frame, text="Pharma Login", style='Pharma.TLabel')
title_label.pack(pady=(0, 10))


ttk.Label(login_frame, text="Username", font=("Arial", 11), background="#ffffff", foreground="#17252a").pack(pady=(0, 3))
username_entry = ttk.Entry(login_frame, style='Pharma.TEntry')
username_entry.pack(ipady=3, pady=(0, 10), padx=20, fill=tk.X)


ttk.Label(login_frame, text="Password", font=("Arial", 11), background="#ffffff", foreground="#17252a").pack(pady=(0, 3))
password_entry = ttk.Entry(login_frame, show="*", style='Pharma.TEntry')
password_entry.pack(ipady=3, pady=(0, 15), padx=20, fill=tk.X)



button_frame = ttk.Frame(login_frame, style='Pharma.TFrame')
button_frame.pack(pady=(0, 10), fill=tk.X, padx=20)

login_button = ttk.Button(button_frame, text="Login", style='Pharma.TButton', command=login)
cancel_button = ttk.Button(button_frame, text="Cancel", style='Cancel.TButton', command=cancel)

login_button.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(0, 5))
cancel_button.pack(side=tk.RIGHT, expand=True, fill=tk.X, padx=(5, 0))

root.mainloop()