class Solution {
public:
    int jump(vector<int>& nums) {
        int l = nums.size();
        int dp[l];
        int index = 0;
        
        
        for(int i=0;i<l;i++)
        {
            dp[i] = 10000;
        }
        
        dp[0] = 0;
        
        for(int i=0;i<l;i++)
        {
            for(int j=nums[i];j>0;j--)
            {
                if(index+j < l)
                {
                    dp[index+j] = min(dp[j+index],1+dp[index]);
                }
            }
            index = index + 1;
        }
        
        return dp[l-1];
        
    }
};
