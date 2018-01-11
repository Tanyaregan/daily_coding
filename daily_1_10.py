# Given a stack of N elements, interleave the first half of the stack with
# the second half reversed using only one other queue.
# This should be done in-place.

# Recall that you can only push or pop from a stack,
# and enqueue or dequeue from a queue.

# For example, if the stack is [1, 2, 3, 4, 5],
# it should become [1, 5, 2, 4, 3].
# If the stack is [1, 2, 3, 4], it should become [1, 4, 2, 3].

# Hint: Try working backwards from the end state.

def reverse_and_interleave(lst):
    """Given a stack of elements, interleave the second half reversed
        into the first half.

    >>> reverse_and_interleave([1, 2, 3, 4, 5])
        [1, 5, 2, 4, 3]

        reverse_and_interleave([1,2,3,4])
        [1, 4, 2, 3]

    """

    i = 1

    while i < len(lst):
        lst[i] = lst.pop()
        i = i + 2

    return lst


#######################################################

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "All tests passed, you super-genius, you."
    print
