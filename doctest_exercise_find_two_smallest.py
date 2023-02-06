
def find_two_smallest(some_list):
    """
    Return a tuple that contains the indices of the two smallest values
    in some_list.

    :param some_list: a list of unique integers
    :precondition: length(some_list) >= 2
    :precondition: some_list does not contain duplicates
    :postcondition: some_list is unchanged
    :postcondition: the indices of the two smallest integers in some_list
    :return: a tuple containing two valid indices corresponding to the two smallest
             values in some_list

    >>> items = [809, 834, 477, 478, 307, 122, 96, 102, 324, 476]
    >>> find_two_smallest(items)
    (6, 7)
    >>> items == [809, 834, 477, 478, 307, 122, 96, 102, 324, 476]
    True
    >>> other_items = [-10, -8, -12, -4, -2]
    >>> find_two_smallest(other_items)
    (0, 2)
    >>> other_items == [-10, -8, -12, -4, -2]
    True
    """
