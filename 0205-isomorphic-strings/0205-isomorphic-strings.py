class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_t = defaultdict(str)
        if len(set(s)) != len(set(t)):
            return False

        for i in range(len(s)):
            if s[i] in s_t and s_t[s[i]] != t[i]:
                return False
            s_t[s[i]] = t[i]
        return True

       
        