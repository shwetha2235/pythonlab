"""This micro-tool presents a fully interactive desktop calculator built using tkinter and organized via the grid
geometry manager. It wires user mouse clicks on graphical Button widgets to internal mathematical
processing engines, updating calculated results dynamically inside a unified Entry display field."""

import tkinter as tk
import math
# Create the main window
root = tk.Tk()
root.title("Multi-Functional Calculator")
root.geometry("350x480")
root.resizable(False, False)
# Calculator display
display = tk.Entry(
    root,
    font=("Arial", 22),
    justify="right",
    borderwidth=5
)
display.grid(
    row=0, column=0, columnspan=4,
    padx=10, pady=15, ipady=10
)
# Button click handler
def click(value):
    if value == "C":
        display.delete(0, tk.END)

    elif value == "⌫":
        current = display.get()
        display.delete(0, tk.END)
        display.insert(0, current[:-1])

    elif value == "=":
        try:
            expression = display.get()
            result = eval(
                expression,
                {"__builtins__": {}},
                {"sqrt": math.sqrt, "pi": math.pi}
            )
            display.delete(0, tk.END)
            display.insert(0, str(result))

        except Exception:
            display.delete(0, tk.END)
            display.insert(0, "Error")

    elif value == "√":
        try:
            number = float(display.get())
            result = math.sqrt(number)
            display.delete(0, tk.END)
            display.insert(0, str(result))

        except Exception:
            display.delete(0, tk.END)
            display.insert(0, "Error")

    elif value == "π":
        display.insert(tk.END, str(math.pi))

    else:
        display.insert(tk.END, value)
# Calculator buttons
buttons = [
    ("C", 1, 0), ("⌫", 1, 1), ("√", 1, 2), ("/", 1, 3),
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("*", 2, 3),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("-", 3, 3),
    ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("+", 4, 3),
    ("0", 5, 0), (".", 5, 1), ("π", 5, 2), ("=", 5, 3)
]
# Create and arrange buttons using grid()
for (text, row, col) in buttons:
    button = tk.Button(
        root,
        text=text,
        font=("Arial", 14),
        width=6,
        height=2,
        command=lambda value=text: click(value)
    )
    button.grid(
        row=row, column=col,
        padx=4, pady=4,
        sticky="nsew"
    )
# Configure grid layout
for col in range(4):
    root.grid_columnconfigure(col, weight=1)

for row in range(6):
    root.grid_rowconfigure(row, weight=1)
# Start the calculator
root.mainloop()
