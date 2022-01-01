class Solution {
public:
    bool canJump(vector<int>& nums) {
        int dp[nums.size()];
        
        for(int i=0;i<nums.size();i++)
        {
            dp[i] =0;
        }
        
        if(nums.size()==1)
        {
            return true;
        }
        
        dp[0] = nums[0];
        
        for(int i=1;i<nums.size();i++)
        {
            if(dp[i-1] > 0)
            {
                dp[i] = max(nums[i],dp[i-1]-1);
            }
        }
        
        if(dp[nums.size()-2] > 0)
        {
            return true;
        }
        
        return false;
    }
};
