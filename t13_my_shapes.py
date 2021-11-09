######################################################################
# Author: Micho Constantino, Luke Wilson, Emmanuel Klinsmann
# Username: constantinom, wilsonl, klinsmann
#
# Assignment: T13: Intro to Classes
#
# Purpose:  Demonstrate the collaboration between out two classes, such as running user input though them
######################################################################

import t13_shape as shape
import turtle


def main():
    """
    takes user input, runs through our classes, and returns a shape based off input

    return: None
    """
    x = int(input("how many sides would you like your shape to have? "))
    y = int(input("how many pixels long would you like the sides to be? "))

    wn = turtle.Screen()  # makes screen

    s = shape.Shape(x, y)           # takes input from above and runs it through class Shape
    s.draw_shape(x, y)              # runs through draw_shape object
    wn.mainloop()


if __name__ == "__main__":
    main()
