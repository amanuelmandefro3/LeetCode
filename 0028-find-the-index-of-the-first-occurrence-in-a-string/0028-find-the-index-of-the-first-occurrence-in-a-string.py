class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        i = j = 0

        while i < len(haystack):
            ans = i
            while j < len(needle) and i < len(haystack) and haystack[i] == needle[j]:
                j += 1
                i += 1
            if j == len(needle):
                return ans
            i = ans + 1
            j = 0


        return -1                
        