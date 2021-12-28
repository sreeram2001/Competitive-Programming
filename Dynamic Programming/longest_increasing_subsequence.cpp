class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        
        int dp[nums.size()];
        
        for(int i=0;i<nums.size();i++)
        {
            dp[i] = 1;
        }
        
        for(int i=1;i<nums.size();i++)
        {
            for(int j=0;j<i;j++)
            {
                if(nums[i] > nums[j])
                {
                    dp[i] = max(dp[i],1+dp[j]);
                }
            } 
        }
        
        int maxi = 0;
        for(int i=0;i<nums.size();i++)
        {
            if(dp[i]>=maxi)
            {
                maxi = dp[i];
            }
        }
        
        return maxi;
        
        
}};
