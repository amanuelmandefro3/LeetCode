class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0
        
class MapSum:

    def __init__(self):
        self.root = TrieNode()
        self.keys = {} 
        

    def insert(self, key: str, val: int) -> None:
        new_val = val
        if key in self.keys:
            new_val = val- self.keys[key]
        self.keys[key]=  val
        val = new_val

        curr = self.root
        for c in key:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
            curr.count += val


    def sum(self, prefix: str) -> int:
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return 0
            curr = curr.children[c]
        return curr.count        
    
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)