import turtle
from turtle import *
import random
from colorgram import *


def draw_random_colored_circle():
    random_color = random.choice(colors)

    timmy_the_turtle.color(random_color.rgb)
    timmy_the_turtle.fillcolor(random_color.rgb)
    timmy_the_turtle.down()
    timmy_the_turtle.dot(20)
    timmy_the_turtle.up()


timmy_the_turtle = Turtle()
timmy_the_turtle.shape("circle")
timmy_the_turtle.setheading(0)
colormode(255)
timmy_the_turtle.hideturtle()
colors = extract("image.jpg", 100)


for i in range(0, 10):
    for _ in range(0, 10):
        draw_random_colored_circle()
        timmy_the_turtle.forward(40)

    if i % 2 == 0:
        timmy_the_turtle.setheading(90)
        timmy_the_turtle.forward(40)
        timmy_the_turtle.setheading(180)
        timmy_the_turtle.forward(40)
    else:
        timmy_the_turtle.setheading(90)
        timmy_the_turtle.forward(40)
        timmy_the_turtle.setheading(0)
        timmy_the_turtle.forward(40)

turtle.done()
