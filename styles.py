import tkinter.ttk as ttk

# Custom style setup for Pharma Login UI
def setup_styles():
    style = ttk.Style()
    style.theme_use('clam')  # Use a modern theme
    style.configure('Pharma.TFrame', background='#ffffff', borderwidth=2, relief='ridge')
    style.configure('Pharma.TLabel', background='#ffffff', foreground='#3aafa9', font=('Arial', 18, 'bold'))
    style.configure('Pharma.TButton', font=('Arial', 11, 'bold'), background='#3aafa9', foreground='#ffffff', borderwidth=0, padding=6)
    style.map('Pharma.TButton', background=[('active', '#2b7a78')], foreground=[('active', '#ffffff')])
    style.configure('Cancel.TButton', font=('Arial', 11, 'bold'), background='#17252a', foreground='#ffffff', borderwidth=0, padding=6)
    style.map('Cancel.TButton', background=[('active', '#3aafa9')], foreground=[('active', '#ffffff')])
    style.configure('Pharma.TEntry', fieldbackground='#e3f6f5', foreground='#17252a', font=('Arial', 11))
    return style
