def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    if input_list is None or number is None or len(input_list) == 0:
        return -1

    if len(input_list) == 1:
        return 0 if input_list[0] == number else -1

    l = find_min_index(input_list)
    u = (l - len(input_list) -1) % len(input_list)

    if input_list[l] == number:
        return l
    if input_list[u] == number:
        return u

    while u != (l + 1) % len(input_list):
        middle = (((u - l) % len(input_list)) // 2 + l) % len(input_list)

        if input_list[middle] == number:
            return middle
        elif input_list[middle] > number:
            u = middle
        else:
            l = middle

    return -1

def find_min_index(input_list):
    
    l = 0
    u = len(input_list)

    while u - l > 1:
        middle = (l + u) // 2
        if input_list[middle] > input_list[l]:
            l = middle
        else:
            u = middle

    return l if input_list[l] < input_list[u] else u

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    sol = test_case[2]
    assert(rotated_array_search(input_list, number) == sol)
    

if __name__ == "__main__":
    test_function([[4,5,6,7,0,1,2,3],2,6])
    test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6, 0])
    test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1, 5])
    test_function([[6, 7, 8, 1, 2, 3, 4], 8, 2])
    test_function([[6, 7, 8, 1, 2, 3, 4], 1, 3])
    test_function([[6, 7, 8, 1, 2, 3, 4], 10, -1])
    test_function([[6], 6, 0])  # Size 1 lists
    test_function([[6], 10, -1])
    test_function([[6, 2], 6, 0]) # Size 2 lists
    test_function([[6, 2], 2, 1])
    test_function([[6, 2], 10, -1])
    test_function([[], 1, -1]) # Empty list
    test_function([None, 1, -1]) # Null inputs
    test_function([[], None, -1])