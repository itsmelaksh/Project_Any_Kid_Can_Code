'''
Importing two libraries:
1. turtle is our own friend
2. random - introducing new library which will help to
            select the random values to have different color
            at each square
'''
import turtle
import random


# picked 5 colors, you can select more but make it sure it exists
# another data type list is introduced. Here color is list
color = ["red", "green", "black", "blue", "yellow"]

#defining shape of turtle
jumper = turtle.Pen()
jumper.shape("turtle")

def squareShape(side):
    '''
    Name: Square shape
    use: you pass the length in side and it will create a square of that shape
    '''
    times=0
    while times < 4:
        jumper.forward(side)
        jumper.left(90)
        times = times + 1

for j in range(50):
    # hiding the turtle, if you want to see comment this line
    jumper.hideturtle()
    # setting the speed to 0 which is fastest and slowest is 10
    jumper.speed(0)

    # picking up the random color name from the above defined list color
    jumper.color(random.choice(color))

    # fill color inside the square created
    jumper.begin_fill()

    # Calling function to create square of length provided
    squareShape(random.randint(15,100))

    # end fill color in the figure created
    jumper.end_fill()
    # you can replace the above code with if condition to understand it better
    # if j != 0:
    #     #calling the function to
    #     squareShape(5+((j*10)*2))
    # else:
    #     squareShape(5)

    # up will not make any line when jumper moves
    # below steps to change the location so that next square starts from new position
    jumper.up()
    jumper.goto(random.randint(-200, 200), random.randint(-200, 200))
    jumper.down()

