class Square:
    """
    This class defines a square by a private instance attribute __size and public instance methods to calculate its area and print it using the # character.
    """
    def __init__(self, size=0):
        """
        Initializes a Square instance with an optional size.

        :param size: The size of the square.
        :type size: int
        :raises TypeError: If size is not an integer.
        :raises ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieves the size of the square.

        :return: The size of the square.
        :rtype: int
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        :param value: The size of the square.
        :type value: int
        :raises TypeError: If value is not an integer.
        :raises ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculates and returns the area of the square.

        :return: The area of the square.
        :rtype: int
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square using the # character.
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
