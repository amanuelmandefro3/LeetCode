class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp = [questions[i][0] for i in range(len(questions))]
        for i in range(len(questions)):
            if i + questions[i][1]+1 < len(questions):
                dp[i + questions[i][1]+1] += dp[i]
        return max(dp)
        