class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if word.count(ch) == 0:
            return word
            
        i = 0
        while i < len(word) and word[i] != ch:
            i += 1
        return word[i::-1] + word[i+1:]    
        