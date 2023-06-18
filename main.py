import math
import random
import tkinter as tk

class Main:
    def __init__(self):
        # set window settings
        self.window_width = 1920
        self.window_height = 1080
        # initialize line length
        self.line_length = 0
        # create a tkinter root window
        self.root = tk.Tk()
        # create a canvas to draw on
        self.canvas = tk.Canvas(self.root, width = self.window_width, height = self.window_height)
        self.canvas.pack()
        # start the update loop
        self.update()

    def update(self):
        # increment line length by 2
        self.line_length += 2
        # clear the canvas
        self.canvas.delete("all")
        # configure the canvas settings to have a black background and no border
        self.canvas.configure(bg = "black", highlightthickness = 0)
        # draw the recursive tree with a line length of 10, a line angle of 30, and a starting x and y of 960 and 840
        self.draw_stick(self.line_length, 0, 960, 840, 10, 30)
        # call the update function again after 13 milliseconds
        self.root.after(13, self.update)

    def draw_stick(self, line_length, line_angle, x, y, length_step, line_angle_step):
        # calculate the x and y size of the line
        x_size = line_length * math.cos(math.radians(line_angle - 90))
        y_size = line_length * math.sin(math.radians(line_angle - 90))
        # generate a random color for a line in hexadecimal 
        color = "#" + "".join(random.choices("0123456789ABCDEF", k = 6))
        # draw the line on the canvas
        self.canvas.create_line(x, y, x + x_size, y + y_size, fill=color)
        # if the line length is greater than or equal to 1
        if line_length >= 1:
            # recursively draw branches of the tree
            self.draw_stick(line_length - length_step, line_angle - line_angle_step, x + x_size, y + y_size, length_step, line_angle_step)
            self.draw_stick(line_length - length_step, line_angle + line_angle_step, x + x_size, y + y_size, length_step, line_angle_step)

if __name__ == "__main__":
    # create an instance of the Main class, and start the Tkinter event loop
    Main().root.mainloop()