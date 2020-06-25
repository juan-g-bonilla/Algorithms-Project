def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if ints is None or len(ints) == 0:
        return None, None

    min = ints[len(ints) -1]
    max = min

    for i in range(len(ints) // 2):
        max_p = ints[i]
        min_p = max_p

        if ints[i+1] > max_p: # First comparison
            max_p = ints[i+1]
        else:
            min_p = ints[i+1]

        if max_p > max: # Second comparison
            max = max_p
        if min_p < min: # Third comparison
            min = min_p

    return min, max

if __name__ == "_main":
    import random

    l = [i for i in range(0, 10)]  # a list containing 0 - 9
    for i in range(5): # Test 5 different random shuffles
        random.shuffle(l)
        assert ((0, 9) == get_min_max(l))

    assert(get_min_max([1]) == (1, 1))
    assert(get_min_max([]) == (None, None))
    assert(get_min_max(None) == (None, None))