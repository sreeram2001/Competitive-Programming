class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        
        int window=0, mini = 100000, start=0;
        
        for(int i=0;i<nums.size();i++)
        {
            window = window + nums[i];
            
            while(window >= target)
            {
                mini = min(mini,i+1-start);
                window = window - nums[start];
                start = start + 1;
            }
        }
        
        if(mini != 100000)
        {
            return mini;
        }
        else
        {
            return 0;
        }
    }
};
