# Given a stack of N elements, interleave the first half of the stack with
# the second half reversed using only one other queue.
# This should be done in-place.

# Recall that you can only push or pop from a stack,
# and enqueue or dequeue from a queue.

# For example, if the stack is [1, 2, 3, 4, 5],
# it should become [1, 5, 2, 4, 3].
# If the stack is [1, 2, 3, 4], it should become [1, 4, 2, 3].

# Hint: Try working backwards from the end state.

def reverse_and_interleave_list(lst):
    """Given a list of elements, interleave the second half reversed
        into the first half.

    >>> reverse_and_interleave_list([1, 2, 3, 4, 5])
    [1, 5, 2, 4, 3]

        reverse_and_interleave_list([1, 2, 3, 4])
    [1, 4, 2, 3]

    """

    i = 1

    while i < len(lst):
        lst.insert(i, lst.pop())
        i = i + 2

    return lst


def reverse_and_interleave_stack(stack):
    """Given a stack of elements, interleave the second half reversed
        into the first half using a queue. """

# I'm going to pseudocode this, I'm not sure if it's possible
# to do it this way with Python.
# This is what I want to do using the [1, 2, 3, 4, 5] example:

# stack = [1, 2, 3, 4, 5]
# queue = []

# Pop each element off the top of the stack and enqueue it:

# queue = [1, 2, 3, 4, 5]
# stack = []

# Take an element from the head of the queue, add it to top of the stack,
# and then take one from the tail and add it to the stack until you have:

# stack = [3, 4, 2, 5, 1]
# queue = []

# Pop each element off the top of the stack and enqueue it:

# queue = [3, 4, 2, 5, 1]
# stack = []

# take each tail out of the queue in turn and add it to the stack:

# stack = [1, 5, 2, 4, 3]
# queue = []



#######################################################

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "All tests passed, you super-genius, you."
    print
