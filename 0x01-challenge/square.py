#!/usr/bin/python3
""" Square class """


class Square:
    """ A class representing a square shape """


    def __init__(self, width=0, height=0):
        """ Initializes a square with the given width and height """
        self.width = width
        self.height = height

    def area_of_my_square(self):
        """ Calculates the area of the square """
        return self.width * self.height

    def perimeter_of_my_square(self):
        """ Calculates the perimeter of the square """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ Returns a string representation of the square """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
