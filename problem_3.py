def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if input_list is None:
        return None

    input_list = mergesort(input_list)
    sol = [0, 0]
    for i, j in enumerate(input_list):
        sol[i % 2] += 10 ** (i // 2) * j
    
    return sol

def mergesort(arr):
    
    if len(arr) <= 1:
        return arr
    
    left, right = [], []

    for i, j in enumerate(arr):
        (left if i <= len(arr) // 2 // 2 else right).append(j)

    left = mergesort(left)
    right = mergesort(right)
    
    return merge(left, right)
    
def merge(left, right):
    
    li, ri = 0, 0
    sol = []
    
    while li < len(left) and ri < len(right):
        if left[li] < right[ri]:
            sol.append( left[li] )
            li += 1
        else:
            sol.append( right[ri] )
            ri += 1
            
    sol += left[li:] + right[ri:]
    return sol

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    assert(sum(output) == sum(solution))

if __name__ == "__main__":
    test_function([[1, 2, 3, 4, 5], [542, 31]])
    test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
    test_function([[4, 6], [6, 4]])
    test_function([[4], [4]])
    test_function([[], []])
    assert(rearrange_digits(None) == None)