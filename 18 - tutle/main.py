from turtle import Turtle, Screen
import random

# challenge 3
def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tp.forward(100)
        tp.right(angle)


tp = Turtle()
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]


# challenge 1
for _ in range(4):
    tp.forward(100)
    tp.left(90)

# challenge 2
for _ in range(15):
    tp.forward(10)
    tp.penup()
    tp.forward(10)
    tp.pendown()


# challenge 3
for shape_side_n in range(3, 11):
    tp.color(random.choice(colours))
    draw_shape(shape_side_n)


# challenge 4
tp.pensize(15)
tp.speed("fastest")
for _ in range(200):
    tp.color(random.choice(colours))
    tp.forward(30)
    tp.setheading(random.choice(directions))



screen = Screen()
screen.exitonclick()
