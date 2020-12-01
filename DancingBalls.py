'''
Program to make rectangle and make it move in canvas
'''
# importing important libraries - we already know about all of them
from tkinter import *
import random
import time

# defining colors so that everytime you run this program will have different color rectangle
color = ["red", "green", "black", "blue", "yellow"]

# creating an instance of tkinterface
tk = Tk()

# deciding height and width of the canvas, we will pass this while creating canvas below
# WIDTH and HEIGHT are constant to give your program more understanding
WIDTH = 500
HEIGHT = 500

# creating our playground
canvas = Canvas(tk, width=WIDTH, height=HEIGHT, bg=random.choice(color))
canvas.pack()


# creating widget i.e, rectangle and oval here and assigning it to variable
rectangle = canvas.create_rectangle(10,20,60,60,fill=random.choice(color))
circle = canvas.create_oval(20,20,50,50,fill=random.choice(color))

# deciding the speed of the rectangle to move
# again both are variables and positive value will make it move forward and vice versa
moveXCoord = 1
moveYCoord = 3
moveXCoord_circle = 4
moveYCoord_circle = 1

# function to keep track of position
def checkBoundary(shape, moveXCoord, moveYCoord):
    '''
    This function will check the current position
    in case figures is moving out of canvas
    it will change the movement to negative
    and (negative negative makes positive)
    So, it will work iteratively
    :return: new position to move
            negative means move backward
            positive means move forward
    '''
    pos = canvas.coords(shape)
    if pos[3] >= HEIGHT or pos[1] <= 0:
        moveYCoord = -moveYCoord
    if pos[2] >= WIDTH or pos[0] <= 0:
        moveXCoord = -moveXCoord
    return moveXCoord, moveYCoord

# Introducing infinite loop
# it will run the program till you wont close it
while True:
    canvas.move(rectangle, moveXCoord, moveYCoord)
    canvas.move(circle, moveXCoord_circle, moveYCoord_circle)
    moveXCoord, moveYCoord = checkBoundary(rectangle, moveXCoord, moveYCoord)
    moveXCoord_circle, moveYCoord_circle = checkBoundary(circle, moveXCoord_circle, moveYCoord_circle)

    tk.update()
    time.sleep(0.001)

tk.mainloop()


