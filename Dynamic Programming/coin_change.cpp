class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        
        int dp[coins.size()+1][amount+1];
        
        for(int i=0;i<coins.size()+1;i++)
        {
            for(int j=0;j<amount+1;j++)
            {
                dp[i][j] = 0;
            }
        }
        
        for(int j=0;j<amount+1;j++)
        {
            dp[0][j] = 1000000; 
        }
        
        
        for(int i=1;i<coins.size()+1;i++)
        {
            for(int j=1;j<amount+1;j++)
            {
                if(j >= coins[i-1])
                {
                    dp[i][j] = min(dp[i-1][j], 1 + dp[i][j-coins[i-1]]);
                }
                
                else
                {
                    dp[i][j] = dp[i-1][j];
                }
            }
        }
        
        if(dp[coins.size()][amount] >= amount+1)
        {
            return -1;
        }
        else
        {
            return dp[coins.size()][amount];
        }
    }
};
