class Solution:
    def numSquares(self, n: int) -> int:
        
        if n <=1 :
            return n
        
        #initialise dp array
        dp = [0 for i in range(n+1)]
        
        dp[0] = 0
        dp[1] = 1       #base cases
        
        #iterate from 2-n
        for i in range(2,n+1):
            mini = float("inf")
            j = 1
            
            #to iterate from 1 to until square(i)
            
            while j*j <= i:             #e.g (2^2 <= 4, j=2, i=4) in case of n=4
                
                mini = min(mini,1+dp[i-j*j])    #eg. ( dp[4] = min(mini,1+dp[4-(2*2)]))
                j = j + 1
                
            dp[i] = mini        #update with min numbers required
            
        return dp[n]
