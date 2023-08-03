def inherits_from(obj, a_class):
    """
    Check if the object is an instance of a class that inherited (directly or indirectly)
    from the specified class.

    Parameters:
        obj: Any - The object to check.
        a_class: type - The class to compare against.

    Returns:
        bool: True if the object is an instance of a subclass of the specified class; otherwise, False.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class

# Test cases
if __name__ == "__main__":
    a = True
    if inherits_from(a, int):
        print("{} inherited from class {}".format(a, int.__name__))    # True inherited from class int

    if inherits_from(a, bool):
        print("{} inherited from class {}".format(a, bool.__name__))   # True inherited from class bool

    if inherits_from(a, object):
        print("{} inherited from class {}".format(a, object.__name__)) # True inherited from class object
