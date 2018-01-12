# Given an array of integers, return a new array such that each element
# at index i of the new array is the product of all the numbers
# in the original array except the one at i.

# Solve it without using division and in O(n) time.

# For example, if our input was [1, 2, 3, 4, 5],
# the expected output would be [120, 60, 40, 30, 24].
# If our input was [3, 2, 1], the expected output would be [2, 3, 6].


def element_product_array(array):
    """Takes an array of integers, returns a new array such that each element
    at index i of the new array is the product of all the numbers
    in the original array except the one at i.

    >>> element_product_array([1, 2, 3, 4, 5])
    [120, 60, 40, 30, 24]

    >>> element_product_array([3, 2, 1])
    [2, 3, 6]

    """

    new_array = []
    index = 0

    while len(array) != len(new_array):

        front_product = 1
        back_product = 1

        for num in array[:index]:
            front_product = num * front_product

        for num in array[index + 1:]:
            back_product = num * back_product

        new_num = back_product * front_product

        new_array.append(new_num)

        index += 1

    return new_array

#######################################################

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "All tests passed, you super-genius, you."
    print
