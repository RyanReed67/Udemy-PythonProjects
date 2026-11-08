# import turtle
# tim = turtle.Turtle()

# import turtle as t
# timmy = t.Turtle()

import turtle
from turtle import Turtle, Screen
import random

timmy = Turtle()
turtle.colormode(255)
timmy.shape("turtle")

# for _ in range(15):
#     timmy.forward(10)
#     timmy.color("white")
#     timmy.forward(10)
#     timmy.color("black")

# for _ in range(15):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()

# colors = ["red", "green", "orange", "blue", "magenta", "cyan",
#           "darkorange", "seagreen", "dodgerblue", "purple"]
# def draw_shape(num_sides):
#     timmy.color(random.choice(colors))
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         timmy.forward(100)
#         timmy.right(angle)
#
# # Call the function for shapes from 3 to 10 sides
# for sides in range(3, 11):
#     draw_shape(sides)

# timmy.shape("turtle")
# timmy.color("red")
#
# for _ in range(4):
#     timmy.forward(100)
#     timmy.right(90)

# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     color = (r, g, b)
#     return color
#
# directions = [0, 90, 180, 270]
# timmy.pensize(10)
# timmy.speed("fastest")
#
#
# for _ in range(200 ):
#     timmy.color(random_color())
#     timmy.forward(30)
#     timmy.setheading(random.choice(directions))

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

timmy.speed("fastest")

def draw_spi(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)

draw_spi(2)





screen = Screen()
screen.exitonclick()
