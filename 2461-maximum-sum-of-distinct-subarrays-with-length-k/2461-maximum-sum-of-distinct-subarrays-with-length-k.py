class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        max_sum, window = 0, defaultdict(int)
        l, current_sum = 0, 0
        
        for r in range(len(nums)):
            window[nums[r]] += 1
            current_sum += nums[r]
            while window[nums[r]] > 1 or len(window) > k:
                window[nums[l]] -= 1
                if window[nums[l]] == 0:
                    del window[nums[l]]
                current_sum -= nums[l]    
                l += 1
            if len(window) == k:
                max_sum = max(max_sum, current_sum)

        return max_sum           
            


        