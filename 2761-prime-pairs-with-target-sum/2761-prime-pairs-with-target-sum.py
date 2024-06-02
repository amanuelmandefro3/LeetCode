class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        prime = [True for _ in range(n)]
        primes = {}
        d = 2
        while d <= n**0.5:
            if prime[d]:
                # primes.add(d)
                i = d*2
                while i < n:
                    prime[i] = False
                    i += d
            d += 1
        for i in range(2,n):
            if prime[i]:
                primes[i] = False    
        ans = []

        for p in primes:
            if not primes[p] and n-p in primes:
                ans.append([p, n-p])
                primes[n-p] = True
        return ans            

        