def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number is None or number < 0:
        return None

    if number < 2:
        return int(number)

    l = 0
    u = number

    while l < u:
        middle = (l + u) // 2
        if middle ** 2 <= number and (middle+1)**2 > number:
            return middle
        elif middle ** 2 > number:
            u = middle
        else:
            l = middle

    return None

if __name__ == "__main__":
    for i, j in ((None, None), (-1, None), (0,0), (1,1), (9,3), (16,4), (27,5)):
        assert(sqrt(i) == j)