class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
        def inbound(row, col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))
        p = 0
        stack = [(0,0)]
        visited[0][0] = True
        while stack:
            curr_row, curr_col = stack.pop()
            if grid[curr_row][curr_col] == 1:
                for row_change, col_change in directions:
                    new_row = curr_row + row_change
                    new_col = curr_col+ col_change
                    if not(inbound(new_row, new_col) and grid[new_row][new_col]):
                        p += 1
            for row_change, col_change in directions:
                new_row = curr_row + row_change
                new_col = curr_col + col_change
                if inbound(new_row, new_col) and not visited[new_row][new_col]:
                    visited[new_row][new_col] = True
                    stack.append((new_row, new_col))
                               



        # def dfs(row, col):
        #     nonlocal p
        #     visited[row][col] = True
        #     if grid[row][col] != 0:
        #         for i, j in directions:
        #             if not (inbound(row+i, col+j) and grid[row+i][col+j]):
        #                 p += 1          

        #     for row_change, col_change in directions:
        #         new_row = row + row_change
        #         new_col = col + col_change
        #         if inbound(new_row , new_col) and not visited[new_row][new_col]:
        #             dfs(new_row, new_col)
        # dfs(0, 0)

        return p                       




