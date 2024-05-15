class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        def dp(i, last):
            if i == len(nums):
                return 0
            
            if (i, last) not in memo:
                include = 0
                if last == -1 or nums[last] < nums[i]:
                    include = 1+dp(i+1, i)
                exclude = dp(i+1, last) 
                memo[(i, last)] = max(exclude, include)     

            return memo[(i, last)]

        return dp(0,-1)
        