We implement mergesort because it has guaranteed O(n log n) (we don't have to worry about worst cases with O(n^2)). 
This however has higher additional space requirements. If memory was an issue, we may consider implementing quicksort which can be performed in-place.

Once the array is sorted, we iterate once through it to reach the solution, an operation that is O(n). The sort + iteration is then O(n log n) + O(n), thus the
total time complexity is O(n log n)