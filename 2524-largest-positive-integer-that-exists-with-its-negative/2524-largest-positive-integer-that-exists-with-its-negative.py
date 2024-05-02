class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums = set(nums)
        _mx = -1
        for num in nums:
            if -num in nums:
                if num < 0:
                    _mx = max(_mx, -num)
                else:
                    _mx = max(_mx, num)    
        return _mx

        