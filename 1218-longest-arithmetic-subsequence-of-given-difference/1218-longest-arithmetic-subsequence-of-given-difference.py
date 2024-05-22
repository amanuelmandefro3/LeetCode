class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = defaultdict(int)

        for i in range(len(arr)):
            dp[arr[i]] = max(dp[arr[i]], dp[arr[i]-difference]+1)
        print(dp)
        val = list(dp.values())
        return max(val)    
