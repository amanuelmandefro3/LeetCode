class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.is_end = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        curr = self.root
        for c in word:
            index = ord(c)-ord('a')
            if not curr.children[index]:
                curr.children[index] = TrieNode()
            curr = curr.children[index]
        curr.is_end = True    

    def find_root(self, word):
        curr = self.root
        for i in range(len(word)):

            if curr.children[ord(word[i])-ord('a')]:
                if curr.children[ord(word[i])-ord('a')].is_end:
                    return word[:i+1]
                curr = curr.children[ord(word[i])-ord('a')]
            else:
                return word               
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for word in dictionary:
            trie.insert(word)
        successors = sentence.split()
        sentences = successors

        for i in range(len(successors)):
            root = trie.find_root(successors[i])
            sentences[i] = root
    
        return ' '.join(sentences)        


        