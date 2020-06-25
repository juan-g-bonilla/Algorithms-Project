rotated_array_search() operates in O(log n). The first step is finding the index of the minimum on the array, which can be done in O(log n) in the function
find_min_index(). In this function, half of the remaining array is discarded from the search in every iteration, meaning we have a O(log n). 
Once we know the index of minimum, we can implement a binary search algorithm slightly modified to take into account that the lowest element 
is not in 0, but instead in the index found previously.

The space complexity is O(1), since we are using a constant number of variables in each algorithm.