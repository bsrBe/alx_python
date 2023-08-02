""" This module defines a Square class that represents a square shape. """

class Square:
    """
    This class defines a square by a private instance attribute __size and a public instance method to calculate its area.
    """
    def __init__(self, size=0):
        """
        Initializes a Square instance with an optional size.

        :param size: The size of the square.
        :type size: int
        :raises TypeError: If size is not an integer.
        :raises ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Calculates and returns the area of the square.

        :return: The area of the square.
        :rtype: int
        """
        return self.__size ** 2
