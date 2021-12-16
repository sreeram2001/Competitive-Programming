class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        if len(grid) == 1:
            return sum(grid[0])
        
        dp = grid
        
        for i in range(1,len(grid[0])):
            dp[0][i] = dp[0][i-1] + dp[0][i]
            
        for i in range(1,len(grid)):
            dp[i][0] = dp[i][0] + dp[i-1][0]
            
        for i in range(1,len(grid)):
            for j in range(1,len(grid[0])):
                dp[i][j] = dp[i][j] + min(dp[i-1][j], dp[i][j-1])
                
        
        return dp[-1][-1]
            
        
