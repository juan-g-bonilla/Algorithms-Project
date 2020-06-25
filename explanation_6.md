The chosen algorithm selects pairs of value of array, determines which one is the lower and which one is the larger and then compare those values to the overall minimum and maximum respectively.
By using this algorithm, for every 2 elements in array we perform 3 comparisons. The alternative would be comparing minimum and maximum for each element, which would require more overall needed comparisons.
For the case of integers and small lists the difference between 3 comparisons every 2 values vs 4 comparisons every 2 values is negligible. 
However, if we were comparing objects for which the compare function is expensive, it would make a considerable difference.

The time complexity is O(n), since we iterate through (half) the array once. The space complexity is O(1) since a constant number of variables is used.