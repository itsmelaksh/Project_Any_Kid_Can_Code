import tkinter

# create variable to initiate tk
tk = tkinter.Tk()

# canvas or our playground to create images
canvas = tkinter.Canvas(tk,width = 500, height = 300)
canvas.pack()

#adding widget to canvas. I added rectangle
canvas.create_rectangle(10,20,60,60, fill ="black")

tk.mainloop()