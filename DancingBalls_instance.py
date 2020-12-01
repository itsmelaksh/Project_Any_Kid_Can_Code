'''
Creating the different objects using class
Introduction to class will make our code compact and increase
reusabiltiy. In simple, it will be scalable.
'''
# importing required libraries
from tkinter import *
import random
import time


# creating an instance of tkinterface
tk = Tk()

# deciding height and width of the canvas, we will pass this while creating canvas below
# WIDTH and HEIGHT are constant to give your program more understanding
WIDTH = 1200
HEIGHT = 800

# defining colors so that everytime you run this program will have different color rectangle
color = ["red", "green", "black", "blue", "yellow","cyan","white","magenta"]

# defining required shapes, increasing a shape and little change in class can do wonder
shapes = ['oval', 'rectangle']

# creating our playground
canvas = Canvas(tk, width=WIDTH, height=HEIGHT)
canvas.pack()

class widgetObject:
    '''
    Class created widget objects
    Now you can create instance of this and pass the value as oval or rectangle
    it has one more function / method move which will make the figure move

    '''
    def __init__(self, select_shape):
        '''
           It will initiliaze the initival values
           and create the required shape using them
        '''
        self.moveXCoord = random.randint(-10, 10)
        self.moveYCoord = random.randint(-10, 10)
        self.x0 = random.randint(10,200)
        self.x1 = random.randint(10,300)
        self.y0 = random.randint(10,300)
        self.y1 = random.randint(10,200)
        self.color = random.choice(color)
        if select_shape == 'oval':
            self.shape = canvas.create_oval(self.x0, self.y0, self.x1, self.y1, fill=self.color)
        elif select_shape == 'rectangle':
            if random.randint(1,2) == 1:
                self.shape = canvas.create_rectangle(self.x0, self.y0, self.x1, self.y1, fill=self.color)
            else:
                self.shape = canvas.create_rectangle(self.x0, self.y0, self.x1, self.x1, fill=self.color)

    def checkBoundary(self):
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
        pos = canvas.coords(self.shape)
        if pos[3] >= HEIGHT or pos[1] <= 0:
            self.moveYCoord = -self.moveYCoord
        if pos[2] >= WIDTH or pos[0] <= 0:
            self.moveXCoord = -self.moveXCoord
        return self.moveXCoord, self.moveYCoord

    def move(self):
        '''
          It will move the object which passsed to it with x coordinate
          and y coordinate
        '''
        canvas.move(self.shape, self.moveXCoord, self.moveYCoord)
        self.moveXCoord, self.moveYCoord = self.checkBoundary()


'''
new variable create_shape created which keeps list
and then forloop to create 100 shapes of instance

'''
create_shape = []
for _ in range(60):
    create_shape.append(widgetObject(random.choice(shapes)))


'''
this loop will run through the shapes created in list
and make them move
'''
while True:
    for mov_shape in create_shape:
        mov_shape.move()

    tk.update()
    time.sleep(0.01)

tk.mainloop()


