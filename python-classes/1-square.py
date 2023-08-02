class Square:
    """
    This class defines a square by a private instance attribute __size.
    """
    def __init__(self, size=0):
        """
        Initializes a Square instance with an optional size.

        :param size: The size of the square.
        :type size: int
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def dict_(self):
        """
        Returns the dictionary representation of a Square instance.

        :return: The dictionary representation of the Square instance.
        :rtype: dict
        """
        return {'size': self.__size}
