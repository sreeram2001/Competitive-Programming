class Solution {
public:
    int longestOnes(vector<int>& nums, int k) {
        
        int left=0, max_l=0;
        
        for(int i=0;i<nums.size();i++)
        {
            if(nums[i] == 0)
            {
                k = k - 1;
            }
            
            while(k<0)
            {
                if(nums[left]==0)
                {
                    k = k + 1;
                }
                
                left = left + 1;
            }
            
            max_l = max(max_l,i-left+1);
        }
        
        return max_l;
    }
};
