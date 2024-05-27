class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.is_end = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        curr = self.root
        for c in word:
            if not curr.children[ord(c)-ord('a')]:
                curr.children[ord(c)-ord('a')] = TrieNode()
            curr = curr.children[ord(c)-ord('a')]
        curr.is_end = True

    def search_max(self, word, res):
        curr = self.root
        if len(res) > len(word):return res
        for c in word:
            curr = curr.children[ord(c)-ord('a')]
            if not curr.is_end: break

            if curr.is_end:
                if len(res) < len(word) or word < res:
                    res = word
        return res            

  

                      
class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        res = ''
        for word in words:
            res = trie.search_max(res, word)

        return res            
                
                 
        