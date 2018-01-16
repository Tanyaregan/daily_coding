# Given an array of integers, find the first missing positive integer
# in linear time and constant space.

# In other words, find the lowest positive integer that does not exist in the array.
# The array can contain duplicates and negative numbers as well.

# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

# You can modify the input array in-place.


def missing_int(array):
    """Given an array of integers, find the lowest positive int that
    does not exist in the array.

    >>> missing_int([3, 4, -1, 1])
    2

    >>> missing_int([1, 2, 0])
    3
    """

    positive_nums = [num for num in array if num > 0]
    positive_nums.sort()

    pos_num = 1

    for num in positive_nums:
        if num != pos_num:
            return pos_num
        else:
            pos_num += 1

    return pos_num


    #######################################################

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "All tests passed, you super-genius, you."
    print
