class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        range_count = [0]*len(nums)
        for l, r in requests:
            range_count[l] += 1
            if r + 1 < len(nums):
                range_count[r+1] -= 1
        curr_sum = 0
        for i in range(len(nums)):
            curr_sum += range_count[i]
            range_count[i] = curr_sum

        range_count.sort()
        nums.sort()
        ans = 0
        for i in range(len(nums)):
            ans += nums[i]*range_count[i]
        return ans%(10**9 + 7)