TriNode is data structure with space complexity O(n*m) where n is the average word length and m is the amount of words in a trie. This represents the worst case.
The main advantage of a Trie is that characters are shared and not unique for every word, thus the required space will, on average be, < n*m.

The time complexity to add(), exists() and find() is O(n) where n is the length of the word to add, find or check for existance. Space complexity is O(1) since no variables are created.

The time complexity of suffixes() is O(n) where n is the total number of TrieNodes that are descendants of the self TrieNode. Similarly, worst case scenario, space complexity is O(n)