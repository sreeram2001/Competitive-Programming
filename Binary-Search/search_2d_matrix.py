class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        i = 0
        j = len(matrix[0]) - 1
        
        while ((i>=0 and i<len(matrix)) and (j>=0 and j<len(matrix[0]))):
            
            if matrix[i][j] == target:
                return True
            
            elif target < matrix[i][j]:
                j = j - 1
                
            elif target > matrix[i][j]:
                i = i + 1
                
            
        return False
            
                
               
  
