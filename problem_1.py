def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
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

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")