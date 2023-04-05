# Import the required libraries
from tkinter import *

# Create an instance of tkinter frame or window
win=Tk()

# Set the size of the tkinter window
win.geometry("700x500+100+100")

# Create a canvas widget
canvas=Canvas(win, width=500, height=300, bg="skyblue")
canvas.pack(fill=BOTH, expand=1)

#canvas2=Canvas(win, width=500, height=300, bg="green")
#canvas2.pack(fill=BOTH, expand=1)

# Add a line in canvas widget
canvas.create_line(100,100,300,100, fill="green", width=5)
canvas.create_line(300,100,100,20, fill="green", width=5)
canvas.create_line(300,300,100,300, fill="green", width=5)
canvas.create_line(100,300,100,100, fill="green", width=5)

#canvas.create_line(500,500,400,50, fill="red", width=5)


win.mainloop()
