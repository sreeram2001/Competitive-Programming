class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        dp = [0 for i in range(30+max(days))]
        
        for i in range(30+max(days)):
            if i in days:
                dp[i] = min(costs[0]+dp[i-1], costs[1]+dp[i-7], costs[2]+dp[i-30])
            else:
                dp[i] = dp[i-1]
                
        return dp[-1]
                
        
