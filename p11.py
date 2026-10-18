"""This micro-project uses the turtle graphics library to automatically render geometric vector patterns and
recursive fractals (such as a Koch snowflake or logarithmic spirals). It configures custom drawing pens,
dynamic RGB background fills, directional movements, and user-defined screen parameters to produce vibrant
vector graphics."""


import turtle
import colorsys

screen = turtle.Screen()
screen.title("Turtle Pattern Generator")
screen.bgcolor("black")
screen.setup(800, 600)

pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)

def koch(length, level):
    if level == 0:
        pen.forward(length)
    else:
        for angle in [60, -120, 60, 0]:
            koch(length / 3, level - 1)
            pen.left(angle)

def spiral():
    for i in range(100):
        pen.pencolor(colorsys.hsv_to_rgb(i / 100, 1, 1))
        pen.forward(i * 2)
        pen.left(91)

choice = input("Enter 1 for Spiral, 2 for Koch Pattern: ")

if choice == "1":
    spiral()
elif choice == "2":
    pen.penup()
    pen.goto(-200, 100)
    pen.pendown()
    for _ in range(3):
        koch(300, 3)
        pen.right(120)
else:
    print("Invalid choice!")

turtle.done()
