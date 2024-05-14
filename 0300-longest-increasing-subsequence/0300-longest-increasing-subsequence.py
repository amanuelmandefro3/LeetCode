class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        length = [1 for i in range(len(nums))]
        for k in range(len(nums)):
            for i in range(k):
                if nums[i] < nums[k]:
                    length[k] = max(length[k], 1+length[i])
        print(length)
        return max(length)