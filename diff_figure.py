import turtle
import random

toad = turtle.Pen()

color = ["red", "green", "black", "blue", "yellow"]

toad.shape("turtle")
toad.hideturtle()
toad.speed(0)


for i in range(200):
    toad.fillcolor(random.choice(color))
    toad.begin_fill()
    toad.circle(2*i)
    toad.left(10)
    toad.end_fill()


# for j in range(50):
#
#     toad.up()
#     toad.goto(random.randint(-50, 200), random.randint(-50, 200))
#     toad.down()
#     # toad.color(random.choice(color))
#     toad.fillcolor(random.choice(color))
#     toad.begin_fill()
#     shape_sq = random.randint(10,200)
#     for i in range(4):
#         toad.forward(shape_sq)
#         toad.left(90)
#     toad.end_fill()

input()