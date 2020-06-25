RouteTrie is a data structure with space complexity O(n*m) where n is the average amount of path parts and m is the number of routes stored. This represents the worst case.
The main advantage of a RouteTrie is that path parts are shared and not unique for every path, thus the required space will, on average, be < n*m.

The time complexity of Router::add_handler() and Router::lookup() is O(n) where n is the number of characters of the input route path, since we have to iterate over the string to divide the path into path parts. Space complexity is O(n) since the path is stored again in an array with all its path parts.