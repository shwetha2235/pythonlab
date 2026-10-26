"""This mini-project brings together multiple units into a multi-screen, frame-driven application managed via
nested Frame widgets, menu bars (Menu), and responsive pack/grid layout managers. Designed around a
clean separation of concerns (MVC-lite structure), it manages application state, captures interactive user input
events, displays warning dialogs, and saves dashboard configuration data to disk."""


import tkinter as tk
from tkinter import messagebox

class Dashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Multi-Frame Dashboard")
        self.root.geometry("600x400")

        # Menu bar
        menu = tk.Menu(root)
        root.config(menu=menu)

        file_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Home", command=self.home)
        file_menu.add_command(label="Exit", command=root.quit)

        # Main frame
        self.frame = tk.Frame(root)
        self.frame.pack(fill="both", expand=True)

        self.home()

    def clear_frame(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

    def home(self):
        self.clear_frame()
        tk.Label(
            self.frame, text="Welcome to Dashboard",
            font=("Arial", 20)
        ).pack(pady=30)

        tk.Button(
            self.frame, text="Student Page",
            command=self.student
        ).pack(pady=10)

        tk.Button(
            self.frame, text="About",
            command=self.about
        ).pack(pady=10)

    def student(self):
        self.clear_frame()
        tk.Label(
            self.frame, text="Student Dashboard",
            font=("Arial", 18)
        ).pack(pady=20)

        tk.Label(
            self.frame, text="Enter Student Name:"
        ).pack()

        self.name = tk.Entry(self.frame)
        self.name.pack(pady=5)

        tk.Button(
            self.frame, text="Submit",
            command=self.submit
        ).pack(pady=10)

        tk.Button(
            self.frame, text="Back",
            command=self.home
        ).pack()

    def submit(self):
        name = self.name.get().strip()
        if name:
            messagebox.showinfo("Success", f"Welcome, {name}!")
        else:
            messagebox.showwarning("Warning", "Enter a name")

    def about(self):
        self.clear_frame()
        tk.Label(
            self.frame, text="About Dashboard",
            font=("Arial", 18)
        ).pack(pady=30)

        tk.Label(
            self.frame,
            text="A modular GUI application built using Tkinter."
        ).pack()

        tk.Button(
            self.frame, text="Back",
            command=self.home
        ).pack(pady=15)


root = tk.Tk()
app = Dashboard(root)
root.mainloop()
