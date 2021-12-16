class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        
        r = len(dungeon)
        c = len(dungeon[0])
        
        dp =[[0 for i in range(c)] for j in range(r)]
        
        dp[-1][-1] = max(1,1-dungeon[-1][-1])
        
        r = r - 1
        c = c - 1
        
        for i in range(r-1,-1,-1):
            dp[i][c] = max(1, dp[i+1][c] - dungeon[i][c])
            
        for i in range(c-1,-1,-1):
            dp[r][i] = max(1, dp[r][i+1] - dungeon[r][i])
            
        for i in range(r-1,-1,-1):
            for j in range(c-1,-1,-1):
                dp[i][j] = min( max(1,dp[i+1][j] - dungeon[i][j]),max(1, dp[i][j+1] - dungeon[i][j]))
                
                
        return dp[0][0];
