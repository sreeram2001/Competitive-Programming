class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        dp = triangle
        dp[0][0] = triangle[0][0]
        
        for i in range(1,len(triangle)):
            for j in range(len(triangle[i])):
                
                if j == 0:
                    dp[i][j] = triangle[i][j] + dp[i-1][j]
                
                elif j == len(triangle[i])-1:
                    dp[i][j] = triangle[i][j] + dp[i-1][j-1]
                
                else:
                    dp[i][j] = min(dp[i-1][j],dp[i-1][j-1]) + triangle[i][j]
            
        op = min(dp[len(dp)-1])
        return op
                    
                
        
