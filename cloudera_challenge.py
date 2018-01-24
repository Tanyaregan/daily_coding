# Complete the function below.


def mergeStrings(a, b):
    """Merges 2 strings into one by alternately adding items from each string
    and then adding remainder onto the end.

    >>> mergeStrings(['a', 'b', 'c'], ['d', 'e', 'f', 'g'])
    ['a', 'd', 'b', 'e', 'c', 'f', 'g']

    >>> mergeStrings(['a', 'b'], ['c', 'd'])
    ['a', 'c', 'b', 'd']

    >>> mergeStrings(['a', 'b', 'c'], [])
    ['a', 'b', 'c']

    >>> mergeStrings([], [])
    []

    """

    if len(a) != len(b):
        if len(a) < len(b):
            common_len = len(a)
        else:
            common_len = len(b)
    else:
        common_len = len(a)

    merged = []
    index = 0

    while index < common_len:
        merged.append(a[index])
        merged.append(b[index])
        index += 1

    if len(a) > common_len:
        for item in a[index:]:
            merged.append(item)

    if len(b) > common_len:
        for item in b[index:]:
            merged.append(item)

    return merged

    ##########################################################

    # >>> getSortedList(['Louis I', 'Alexander III', 'Alexander VII', 'Louis IV', 'Frances XX'])
    # ['Alexander VII', 'Alexander III', 'Frances XX', 'Louis IV', 'Louis I']

    # >>> getSortedList(['Philip I', 'Phillip II'])
    # ['Phillip II', 'Philip I']

    # >>> getSortedList(['Louis IX', 'Louis VIII'])
    # ['Louis VIII', 'Louis IX']

# def getSortedList(names):
#     """takes a list of names & ordinal numbers, orders them alphabetically and then by reversed ordinals (youngest first)."""

#     ordinals_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50}

#     for title in names:

#         print 'raw title:', title
#         name = title[:title.index(' ')]
#         ordinal = title[(title.index(' ') + 1):]
#         total = 0

#         if len(ordinal) == 1:
#             total = ordinals_dict[ordinal]
#             print 'LENGTH OF ONE total =', total
#             pass

#         else:

#             index = 0

#             for char in ordinal:

#                 print 'index:', index, 'ordinal char:', char

#                 if index >= (len(ordinal) - 1):
#                     # total = total + ordinals_dict[char]
#                     print 'INDEX = LEN-1 total =', total
#                     pass

#                 else:
#                     value = ordinals_dict[ordinal[index]]
#                     next_value = ordinals_dict[ordinal[index + 1]]

#                 if value >= next_value:
#                     total += value
#                     index += 1
#                     print 'Add char to total: running sum =', total

#                 else:
#                     total += (next_value - value)
#                     index += 2
#                     print 'Subtract char from next char: running sum =', total

#         print 'total ordinal value =', total

#         title = name + ' ' + str(total) + ' ' + ordinal

#         print '*** Title =', title
#         print ''


# getSortedList(['Alex XIV', 'Tanya VIII', 'Alex X', 'Tanya VI'])

    #######################################################

def braces(values, n):
    """Determines if n sets of values in an array has balanced open and close brackets.
    returns a array of n strings containing "YES" for balanced brackets, "NO" for unbalanced.

    >>> braces([ '[', '{', '('], 1 )
    ['NO']

    >>> braces( [ '{', '}' ], 1 )
    ['YES']

    >>> braces([ ['(',')'], ['(', ')'] ], 2)
    ['YES', 'YES']

    >>> braces([ ['[', '{', '}', ']'], [ ']' ]], 2 )
    ['YES', 'NO']
    """

# Helper function that evaluates a single string of brackets

    def evaluate_value(value):
        """Evaluates a single string of brackets to determnine if they are balanced.

        >>> evaluate_value([ '[', '{', '(' ])
        'NO'

        >>> evaluate_value( [ '{', '}' ] )
        'YES'
        """

        open_brackets = ['[', '{', '(']
        matching_brackets = set([('(', ')'), ('[', ']'), ('{', '}')])
        bracket_stack = []

    # check the length of value is even, or it's not matched sets

        if len(value) % 2 != 0:
            return 'NO'

    # If the char is an open bracket, add it to the stack.

        else:
            for char in value:
                if char in open_brackets:
                    bracket_stack.append(char)

    # If current char is not an open bracket, and the stack is empty, return false

                else:
                    if len(bracket_stack) == 0:
                        return 'NO'

    # If the current char is not an open bracket and
    # does not match with the top stack char to form a pair, return false

                    else:
                        if (bracket_stack.pop(), char) not in matching_brackets:
                            return 'NO'

    # if nothing has come up "NO", then the answer is "YES"

                        else:
                            return 'YES'

# Now use helper funciton to evaluate each of n strings in values, and return an answer array with
# results for each string in values.

    answer_array = []

    if n == 1:
        answer_array.append(evaluate_value(values))
        return answer_array
    else:
        for array in values:
            answer_array.append(evaluate_value(array))

    return answer_array

    #######################################################

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "All tests passed, you super-genius, you."
    print
