class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        min_row, max_row, min_col, max_col = 0, len(matrix) - 1, 0 , len(matrix[0])-1

        i, j = 0, 0
        ans = []
        while i <= max_row and min_col <= max_col:
           
            # Traverse right
            while j <= max_col:
                ans.append(matrix[i][j])
                j += 1
            j -= 1
            i += 1
            min_row += 1
            
            # Traverse down
            while i <= max_row:
                ans.append(matrix[i][j])
                i += 1
            j -= 1
            i -= 1
            max_col -= 1 

            # Traverse left
            while j >= min_col and i >= min_row:
                ans.append(matrix[i][j])
                j -= 1
            j += 1
            i -= 1
            max_row -= 1

            # Traverse up
            while i >= min_row and j <= max_col:
                ans.append(matrix[i][j])
                i -= 1
            i += 1
            j += 1
            min_col += 1  

        return ans        


        
        