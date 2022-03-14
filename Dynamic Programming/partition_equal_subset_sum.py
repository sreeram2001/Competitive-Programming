class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        tot = sum(nums)
        if (tot%2):
            return False

        n = len(nums)
        dp = [[False for i in range(tot+1)]for j in range(n+1)]
        
        for i in range(n):
            dp[i][0] = True
            
        for j in range(1,tot):
            dp[0][j] = False
            
        for i in range(1,n+1):
            for j in range(1,tot+1):
                
                dp[i][j] = dp[i-1][j]
                if j>=nums[i-1]:
                    dp[i][j] = (dp[i][j]) or (dp[i-1][j-nums[i-1]])
                

        return dp[n][int(tot/2)]
            
        
