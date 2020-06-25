Edge cases 0 and 1 are covered by checking against them at the start of algorithm.

The algorithm runs in O(log(n)) because for each step we are removing from consideration half of the possible integers, much like a binary search algorithm.

Space complexity is O(1) since the number of variables used does not depend on the input