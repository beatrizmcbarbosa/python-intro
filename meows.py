def meow(n: int) -> str:
    # Below, docstring, is a string used to document a Python module, class, function or method
    # It is just a convention, in standard format, to document, in this case, my function
    """
    Meow n times.

    :param n: Number of times to meow
    :type n: int
    :raise TypeError: If n is not an int
    :return: A string of n meows, one per line
    :rtype: str
    """
    return "meow\n" * n


number: int = int(input("Number: "))
meows: str = meow(number)
print(meows)
