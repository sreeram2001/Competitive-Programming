class Solution {
public:
    int maximalSquare(vector<vector<char>>& matrix) {
        
        int r = matrix.size();
        int c = matrix[0].size();
        int maxi = 0;
        int dp[r+1][c+1];
        
        for(int i=0;i<=r;i++)
        {
            for(int j=0;j<=c;j++)
            {
                dp[i][j] = 0;
            }
        }
        
        for(int i=1;i<=r;i++)
        {
            for(int j=1;j<=c;j++)
            {
                if(matrix[i-1][j-1] == '1')
                {
                    dp[i][j] = 1 + min(dp[i-1][j],min(dp[i][j-1],dp[i-1][j-1]));
                    maxi = max(dp[i][j],maxi);
                }
            }
        }
        
    return maxi*maxi;
        
    }
};
