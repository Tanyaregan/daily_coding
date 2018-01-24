# cons(a, b) constructs a pair, and car(pair)
# and cdr(pair) returns the first and last element of that pair.

# For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

# Given this implementation of cons:

# def cons(a, b):
#     return lambda f : f(a, b)

# Implement car and cdr.



    #######################################################

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "All tests passed, you super-genius, you."
    print
