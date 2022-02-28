class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        
        """
        row = []       #index of 0 rows
        col = []       #index of 0 columns
        
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    
                    if r not in row:
                        row.append(r)
                    if c not in col:
                        col.append(c)
                             
        #row-wise
        for r in row:
            matrix[r] = [0 for it in range(len(matrix[r]))]
            
        #column-wise
        for i in range(len(matrix)):
            for c in col:
                matrix[i][c] = 0
            
        
        return matrix
            
                    
