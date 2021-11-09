######################################################################
# Author: Micho Constantino, Luke Wilson, Emmanuel Klinsmann
# Username: constantinom, wilsonl, klinsmann
#
# Assignment: T13: Intro to Classes
#
#
# Purpose: A class for creating shapes. Collaborates with the Points class
######################################################################

import turtle


class Shape:
    """
    A class that makes shapes based on user input
    """

    def __init__(self, sides, length):              # specific size and number of sides
        """
        takes sides from user input (side) and makes them the length of len
        :param sides: number of sides for the shape
        :param length: the shape sides' length
        """
        self.side = sides                           # 4 should make square
        self.len = length                           # determines len of each side

    def draw_shape(self, side, len):
        """
        draws given shape based on the user's input at the speed of 3.
        :param r: the red channel
        :param g: the green channel
        :param b: the blue channel
        """
        tess = turtle.Turtle()
        tess.penup()
        tess.speed(3)
        self.side = side
        self.len = len

        tess.pendown()
        if side == 3:                       # our options are triangle, square, and pentagon
            for i in range(side):
                tess.forward(len)
                tess.left(120)
        elif side == 4:                     # makes square
            for i in range(side):
                tess.forward(len)
                tess.left(90)
        elif side == 5:                     # makes pentagon
            for i in range(side):
                tess.forward(len)
                tess.left(72)

