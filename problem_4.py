def sort_012(input_list):

    if input_list == None:
        return None

    zi = 0
    ti = len(input_list) -1
    
    for i in range(len(input_list)):
        
        if i > ti:
            break
        
        while input_list[i] != 1:
            if input_list[i] == 0:
                
                if i <= zi:
                    zi += 1
                    break
                    
                input_list[zi], input_list[i] = input_list[i], input_list[zi]
                zi += 1

            elif input_list[i] == 2:

                if i >= ti:
                    break

                input_list[ti], input_list[i] = input_list[i], input_list[ti]
                ti -= 1        
    
    return input_list

def test_function(test_case):
    assert(sort_012(test_case) == sorted(test_case))


if __name__ == "__main__":
    test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
    test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
    test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
    test_function([])
    assert(sort_012(None) == None)