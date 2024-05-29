class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n,m = len(s), len(t)
        dp = [[0]*(m+1) for _ in range(2)]
        
        _next = [0]*(m+1)
        _next[-1] = 1
        for i in range(n-1,-1, -1):
            curr = [0]*(m+1)
            curr[-1] = 1
            for j in range(m):
                if s[i] == t[j]:
                    curr[j] = _next[j] + _next[j+1]
                else:
                    curr[j] = _next[j]
            _next = curr        
        print(dp)            
        return _next[0]               
        