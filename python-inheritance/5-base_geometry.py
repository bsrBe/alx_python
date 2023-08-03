class BaseGeometry:
    def area(self):
        """
        Public instance method that raises an Exception with the message 'area() is not implemented'.

        Raises:
            Exception: Always raises an Exception with the message 'area() is not implemented'.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Public instance method that validates the value if it's an integer and greater than 0.

        Parameters:
            name (str): The name of the value being validated.
            value (int): The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.

        Example:
            bg = BaseGeometry()
            bg.integer_validator("my_int", 12)  # Valid
            bg.integer_validator("name", "John")  # Raises TypeError
            bg.integer_validator("age", 0)  # Raises ValueError
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

