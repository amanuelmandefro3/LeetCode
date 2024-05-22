class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n,m = len(matrix), len(matrix[0])
        dp = [[0 if matrix[i][j] == '0' else 1 for j in range(m)] for i in range(n)]
        def prev_ans(r,c):
            if 0 <= r < len(matrix) and 0 <= c < len(matrix[0]):
                return dp[r][c]
            return 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '1':
                    top = min(prev_ans(i-1,j),  prev_ans(i,j-1)) + 1
                    # left = min(prev_ans(i-1,c),  prev_ans(r,j-1)) + 1
                    dp[i][j] = top 
        _mx = 0
        for i in range(n):
            for j in range(m):
                _mx = max(_mx, dp[i][j])
        return _mx*_mx        

        return 9            



        