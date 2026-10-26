"""This image processing mini-tool opens JPEG or PNG images and processes their raw pixel grids by adjusting
underlying RGB color channels. It applies transformations such as grayscale conversion, image thresholding
(black and white generation), and simple spatial blur filters directly before outputting the processed image."""

from PIL import Image, ImageFilter
from tkinter import Tk, filedialog

root = Tk()
root.withdraw()

filename = filedialog.askopenfilename(
    title="Select an image",
    filetypes=[
        ("Image files", "*.png *.jpg *.jpeg"),
        ("All files", "*.*")
    ]
)

if not filename:
    print("No image selected.")
else:
    try:
        img = Image.open(filename)

        print("Image opened successfully.")
        print("Size:", img.size)

        gray = img.convert("L")
        gray.save("grayscale.png")

        bw = gray.point(lambda x: 255 if x > 128 else 0)
        bw.save("black_white.png")

        blur = img.filter(ImageFilter.BLUR)
        blur.save("blurred.png")

        print("Processed images saved successfully.")

    except Exception as e:
        print("Error:", e)

root.destroy()