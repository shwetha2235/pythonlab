""" This utility tool persists live Python object states to disk across execution runs using the built-in pickle and
shelve modules. It converts complex class instances into binary streams, writes them safely to disk, and
reads/restores object states back into memory."""


import pickle
import shelve

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name, "Marks:", self.marks)


s = Student("Ravi", 90)

# Save and restore using pickle
with open("student.dat", "wb") as f:
    pickle.dump(s, f)

with open("student.dat", "rb") as f:
    obj = pickle.load(f)

print("Using Pickle:")
obj.display()

# Save and restore using shelve
with shelve.open("student_db") as db:
    db["student"] = s

with shelve.open("student_db") as db:
    obj = db["student"]

print("\nUsing Shelve:")
obj.display()
