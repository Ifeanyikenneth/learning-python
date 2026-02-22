from turtle import Turtle, Screen
import random


timmy_the_turtle = Turtle()
# Turtle.colormode(255)
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("red")
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# """completing the task from here to be able to draw a square"""
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# # for _ in range(4):
# #     timmy_the_turtle.forward(100)
# #     timmy_the_turtle.right(90)
# """Here we are to make our turtle to draw a Dashed line"""
# for _ in range(15):
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.pendown()
"""Here will are making our Turtle to draw different shape with different color """

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "wheat", "SlateGray", "SeaGreen" ]

def draw_shape(num_side):
    angle = 360 / num_side
    for _ in range(num_side):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(angle)

for shape_side_n in range(3, 11):
    timmy_the_turtle.color(random.choice(colors))
    draw_shape(shape_side_n)



# """Making our turtle to walk on a random walk with bigger size and diff color  """
# colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "wheat", "SlateGray", "SeaGreen" ]
# directions  = [0, 90, 180, 270]
# timmy_the_turtle.pensize(15)
# timmy_the_turtle.speed("fastest")
#
# for _ in range(200):
#     timmy_the_turtle.color(random.choice(colors))
#     timmy_the_turtle.forward(30)
#     timmy_the_turtle.setheading(random.choice(directions))
#
# """Making use of the random color with a Tuple """
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     color = (r, g, b)
#     return color
#
# directions  = [0, 90, 180, 270]
# timmy_the_turtle.pensize(15)
# timmy_the_turtle.speed("fastest")
#
# for _ in range(200):
#     timmy_the_turtle.color(random_color())
#     timmy_the_turtle.forward(30)
#     timmy_the_turtle.setheading(random.choice(directions))
#
#
#
#


screen = Screen()
screen.exitonclick()