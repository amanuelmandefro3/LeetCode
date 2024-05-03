class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        mx = 2**maximumBit -1
        xor, ans = 0, []
        for num in nums:
            xor ^= num
            ans.append(mx^xor)
        return ans[::-1]    


        