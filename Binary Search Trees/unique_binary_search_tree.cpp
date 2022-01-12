class Solution {
public:
    int numTrees(int n) {
        
        int dp[n+1];
        int left_sub=0,right_sub=0;
        dp[0] = 1;
        dp[1] = 1;
        
        for(int i=2; i<n+1; i++)
        {
            dp[i] = 0;
        }
        
        for(int i=2; i<n+1; i++)
        {
            for(int j=1; j<i+1; j++)
            {
                left_sub = j - 1;
                right_sub = i - j;
                dp[i] = dp[i] + (dp[left_sub]*dp[right_sub]);
            }
        }
        
        return dp[n];
    }
};
