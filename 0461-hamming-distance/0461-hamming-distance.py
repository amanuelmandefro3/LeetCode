class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        a, b = bin(x)[2:],bin(y)[2:]
        n = max(len(a), len(b))
        a = '0'*(n-len(a)) + a
        b = '0'*(n-len(b)) + b
        ans = 0

        for i in range(n):
            if a[i] != b[i]:
                ans += 1   
       
        return ans

        