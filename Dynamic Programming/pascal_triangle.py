class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        dp = [[1]]
        
        if numRows == 1:
            return dp
        
        for i in range(1,numRows):
            prev = dp[i-1]
            curr = [None]*(i+1)
            
            curr[0] = prev[0]
            curr[i] = prev[len(prev)-1]
            
            for j in range(0,len(prev)-1):
                curr[j+1] = prev[j] + prev[j+1]
                
            dp.append(curr)
            
        return dp
            
