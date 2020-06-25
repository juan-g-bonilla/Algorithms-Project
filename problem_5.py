class TrieNode(object):
    def __init__(self):
        self.is_word = False
        self.children = {}

    def suffixes(self, suffix = ''):
        """
        Return a list with all possible word endings for this node
        """
        sol = [suffix] if self.is_word else []

        for i, j in self.children.items():
            sol += j.suffixes(suffix + i)

        return sol

class Trie(object):
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, word):
        """
        Add `word` to trie
        """
        node = self.root
        
        for i in word:
            if i not in node.children:
                node.children[i] = TrieNode()
            node = node.children[i]
        
        node.is_word = True
        
    
    def exists(self, word):
        """
        Check if word exists in trie
        """
        node = self.find(word)
        return node is not None and node.is_word

    def find(self, prefix):
        """
        Find node that represents given prefix
        """
        node = self.root
        
        if prefix is None:
            return node

        for i in prefix:
            if i not in node.children:
                return None
            
            node = node.children[i]
            
        return node

if __name__ == "__main__":
    trie = Trie()
    wordList = [
        "ant", "anthology", "antagonist", "antonym", 
        "fun", "function", "factory", 
        "trie", "trigger", "trigonometry", "tripod"
    ]
    for word in wordList:
        trie.add(word)

    assert(trie.find("tr").suffixes() == ["ie", "igger", "igonometry", "ipod"])
    assert(trie.find("ant").suffixes() == ["", "hology", "agonist", "onym"])
    assert(trie.find("f").suffixes() == ["un", "unction", "actory"])
    assert(trie.find("factory").suffixes() == [""])
    assert(trie.find("").suffixes() == wordList)
    assert(trie.find("udacity") == None)

    trie = Trie()
    assert(trie.find("").suffixes() == [])
    assert(trie.find("a") == None)