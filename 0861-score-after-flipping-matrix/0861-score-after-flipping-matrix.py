class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        # Flip rows to ensure first column has all 1s
        for row in grid:
            if row[0] == 0:
                for i in range(cols):
                    row[i] ^= 1  # Flips 0 to 1 and vice versa
        
        # Flip columns to maximize number of 1s in each column
        for col in range(1, cols):
            count_zeros = sum(grid[row][col] == 0 for row in range(rows))
            if count_zeros > rows - count_zeros:
                for row in range(rows):
                    grid[row][col] ^= 1  # Flip if more zeros than ones
        
        # Calculate the total score
        score = 0
        for row in grid:
            score += int(''.join(map(str, row)), 2)
        
        return score
