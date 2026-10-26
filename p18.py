
import tkinter as tk
from tkinter import messagebox, filedialog
import json

records = []

def add_record():
    name = name_entry.get()
    roll = roll_entry.get()
    age = age_entry.get()

    if not name or not roll or not age:
        messagebox.showwarning("Error", "Fill all fields")
        return

    records.append({
        "Name": name,
        "Roll": roll,
        "Age": age,
        "Gender": gender.get(),
        "Courses": [c for c, v in courses.items() if v.get()]
    })

    update_list()
    name_entry.delete(0, tk.END)
    roll_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)

def update_list():
    student_list.delete(0, tk.END)
    for r in records:
        student_list.insert(tk.END, f'{r["Roll"]} - {r["Name"]}')

def delete_record():
    selected = student_list.curselection()
    if selected:
        records.pop(selected[0])
        update_list()
    else:
        messagebox.showwarning("Error", "Select a record")

def save_records():
    file = filedialog.asksaveasfilename(
        defaultextension=".json",
        filetypes=[("JSON files", "*.json")]
    )
    if file:
        with open(file, "w") as f:
            json.dump(records, f, indent=4)
        messagebox.showinfo("Success", "Records saved")

root = tk.Tk()
root.title("Student Record Manager")
root.geometry("400x500")

tk.Label(root, text="Student Record Manager",
         font=("Arial", 16)).pack(pady=10)

tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Roll Number").pack()
roll_entry = tk.Entry(root)
roll_entry.pack()

tk.Label(root, text="Age").pack()
age_entry = tk.Entry(root)
age_entry.pack()

gender = tk.StringVar(value="Female")
tk.Label(root, text="Gender").pack()

for g in ["Male", "Female", "Other"]:
    tk.Radiobutton(root, text=g, variable=gender,
                   value=g).pack()

courses = {
    "Python": tk.BooleanVar(),
    "Java": tk.BooleanVar()
}

for c, v in courses.items():
    tk.Checkbutton(root, text=c, variable=v).pack()

tk.Button(root, text="Add Record",
          command=add_record).pack(pady=5)
tk.Button(root, text="Delete Record",
          command=delete_record).pack(pady=5)
tk.Button(root, text="Save Records",
          command=save_records).pack(pady=5)

student_list = tk.Listbox(root, width=40)
student_list.pack(pady=10)

root.mainloop()
