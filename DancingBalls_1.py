'''
Program to make rectangle and make it move in canvas
'''
# importing important libraries - we already know about all of them
from tkinter import *
import random
import time

# defining colors so that everytime you run this program will have different color rectangle
color = ["red", "green", "black", "blue", "yellow","cyan","white","magenta"]

# creating an instance of tkinterface
tk = Tk()

# deciding height and width of the canvas, we will pass this while creating canvas below
# WIDTH and HEIGHT are constant to give your program more understanding
WIDTH = 800
HEIGHT = 600

# creating our playground
canvas = Canvas(tk, width=WIDTH, height=HEIGHT, bg=random.choice(color))
canvas.pack()

rectangle = []
xy_coord = []
for cr_rect in range(30):
    # creating widget i.e, rectangle here and assigning it to variable
    side = random.randint(50,200)
    rectangle.append(canvas.create_rectangle(10,20,side,side,fill=random.choice(color)))
    # rectangle.append(canvas.create_polygon(80,90,50,60,side,20,fill=random.choice(color)))

    # deciding the speed of the rectangle to move
    # again both are variables and positive value will make it move forward and vice versa
    moveXCoord = random.randint(-10,10)
    moveYCoord = random.randint(-10,10)
    xy_coord.append([moveXCoord,moveYCoord])

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
    for cnt_rect in range(len(rectangle)):
        canvas.move(rectangle[cnt_rect], xy_coord[cnt_rect][0], xy_coord[cnt_rect][1])
        xy_coord[cnt_rect][0], xy_coord[cnt_rect][1] = checkBoundary(rectangle[cnt_rect], xy_coord[cnt_rect][0], xy_coord[cnt_rect][1])

    tk.update()
    time.sleep(0.001)

tk.mainloop()


