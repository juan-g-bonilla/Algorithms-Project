class RouteTrieNode(object):
    def __init__(self, handler = None):
        self.handler = handler
        self.children = {}

class RouteTrie(object):
    def __init__(self, handler = None):
        self.root = RouteTrieNode(handler)
    
    def add(self, route, handler):
        """
        Add `route` to trie
        """
        node = self.root
        
        for i in route:
            if i not in node.children:
                node.children[i] = RouteTrieNode()
            node = node.children[i]
        
        node.handler = handler

    def find(self, route):
        """
        Find node that represents given prefix
        """
        node = self.root
        
        if route is None:
            return node

        for i in route:
            if i not in node.children:
                return None
            
            node = node.children[i]
            
        return node
    
class Router(object):
    def __init__(self, root_h = "root handler", not_found_h = "Error 404: handler not found"):
        self.trie = RouteTrie(root_h)
        self.not_found_h = not_found_h 

    def add_handler(self, route, handler):
        self.trie.add(Router._split_path(route), handler)

    def lookup(self, route):
        if route is None:
            return self.trie.root.handler 

        node = self.trie.find(Router._split_path(route))
        return node.handler if node is not None and node.handler is not None else self.not_found_h

    @staticmethod
    def _split_path(route):
        sol = []
        buffer = ""

        for i in route:
            if i == "/":
                if buffer != "":
                    sol.append(buffer)
                    buffer = ""
            else:
                buffer += i

        if buffer != "":
            sol.append(buffer)

        return sol

if __name__ == "__main__":
    router = Router("root handler", "not found handler")
    router.add_handler("/home/about", "about handler")

    assert(router.lookup(None) == "root handler")
    assert(router.lookup("/") == "root handler")
    assert(router.lookup("/home") == "not found handler")
    assert(router.lookup("/home/about") == "about handler")
    assert(router.lookup("/home/about/") == "about handler")
    assert(router.lookup("/home/about/me") == "not found handler")

    emptyR = Router()

    assert(emptyR.lookup(None) == "root handler")
    assert(emptyR.lookup("") == "root handler")
    assert(emptyR.lookup("nowhere") == "Error 404: handler not found")