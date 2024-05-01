class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        xor = nums[0]
        for i in range(1, len(nums)):
            xor ^= nums[i]

        k, xor = max(xor, k), min(xor, k)

        ans = 0
        while k > 0:
            kbit = k & 1
            xorbit = xor & 1

            ans += kbit ^ xorbit

            k >>= 1
            xor >>= 1

        return ans        
                 
       






        

        return 2    
        