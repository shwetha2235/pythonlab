"""This desktop GUI tool leverages native modal dialogs (filedialog.askopenfilename,
colorchooser.askcolor, messagebox) to allow users to interactively locate, open, and view image files or
text contents on screen. The interface updates canvas components and Label properties dynamically while
binding mouse clicks and keypress events (<Return>) to update application layouts."""


import tkinter as tk
from tkinter import filedialog, colorchooser, messagebox
from PIL import Image, ImageTk

def open_file(event=None):
    file = filedialog.askopenfilename(
        filetypes=[
            ("Images", "*.png *.jpg *.jpeg"),
            ("Text files", "*.txt")
        ]
    )

    if not file:
        return

    try:
        if file.lower().endswith((".png", ".jpg", ".jpeg")):
            img = Image.open(file)
            img.thumbnail((350, 300))
            photo = ImageTk.PhotoImage(img)
            display.config(image=photo, text="")
            display.image = photo
        else:
            with open(file, "r", encoding="utf-8") as f:
                content = f.read()
            display.config(image="", text=content)

        messagebox.showinfo("Success", "File opened successfully!")

    except Exception as e:
        messagebox.showerror("Error", str(e))

def change_color():
    color = colorchooser.askcolor()[1]
    if color:
        display.config(bg=color)

root = tk.Tk()
root.title("Image and File Viewer")
root.geometry("500x450")

tk.Label(root, text="Image / File Viewer",
         font=("Arial", 16)).pack(pady=10)

tk.Button(root, text="Open File",
          command=open_file).pack(pady=5)

tk.Button(root, text="Choose Background Color",
          command=change_color).pack(pady=5)

display = tk.Label(root, text="Open an image or text file",
                   wraplength=450, bg="white")
display.pack(fill="both", expand=True, padx=10, pady=10)

root.bind("<Return>", open_file)
display.bind("<Button-1>", lambda event: open_file())

root.mainloop()
