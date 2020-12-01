'''
Importing two libraries:
1. turtle is our own friend
2. random - introducing new library which will help to
            select the random values to have different color
            at each square
'''
import turtle
import random

#defining shape of turtle
jumper = turtle.Pen()
jumper.shape("turtle")

# picked 5 colors, you can select more but make it sure it exists! Check documentation
# another data type list is introduced. Here color is list
color = ["red", "green", "black", "cyan", "yellow","blue","orange"]



for j in range(50):
    # hiding the turtle, if you want to see comment this line
    jumper.hideturtle()
    # setting the speed to 0 which is fastest and slowest is 10
    jumper.speed(0)

    # bringing our jumper up so that it wont create line and
    # easy to change the location based on random number
    # if you want to see what random is doing print the below statement:
    # print(random.randint(-200, 200))
    jumper.up()
    jumper.goto(random.randint(-200, 200), random.randint(-200, 200))
    jumper.down()

    # select the random fill color from the choice given in list above
    jumper.fillcolor(random.choice(color))

    # begin the fill, whatever image will come after this will be filled with the above color
    jumper.begin_fill()

    # deciding the random radius of the circle between 20 and 100
    # you can directly put random.randint rather than creating variable
    radius = random.randint(20,100)

    # Drawing the circle
    jumper.circle(radius)

    # end fill will stop filling of color and next iteration will change the color
    jumper.end_fill()


input()