class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        numRows = rowIndex + 1
        
        dp = [[1]]
        
        if numRows == 1:
            return dp[0]
        
        for i in range(1,numRows):
            prev = dp[i-1]
            curr = [None]*(i+1)
            
            curr[0] = prev[0]
            curr[i] = prev[len(prev)-1]
            
            for j in range(0,len(prev)-1):
                curr[j+1] = prev[j] + prev[j+1]
                
            dp.append(curr)
            
        return dp[rowIndex]
            
