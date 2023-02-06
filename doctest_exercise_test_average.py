"""
Can you fix this?
"""


def average(values):
    """
    Return the average of the numbers in values.  Some items in values may be
    None, and they are not counted toward the average.

    If there are no numbers in values, the function returns None. If the
    list contains Nones and nothing else, the function returns None.

    :param values: a list of real numbers that may contain None
    :precondition: values is a possiby empty list of real numbers that may contain None
    :postcondition: values is not modified
    :postcondition: calculates the average excluding None
    :return: the average of the non-None numbers in values as a float

    >>> average([20, 30])
    25.0
    >>> average([None, 20, 30])
    25.0
    >>> average([0])
    0.0
    >>> result = average([None, None, None])
    >>> result is None
    True
    >>> empty_list = []
    >>> result = average(empty_list)
    >>> result is None
    True
    """

