class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        
        int count=1,maxi=0;
        
        if(nums.size() == 0)
        {
            return 0;
        }
        
        sort(nums.begin(),nums.end());
        
        for(int i=1;i<nums.size();i++)
        {
            if(nums[i] != nums[i-1])
            {

            if(nums[i] == 1+nums[i-1])
            {
                count = count + 1;
            }
            else
            {
                maxi = max(maxi,count);
                count = 1;
            }
            }
        }
        
        return max(maxi,count);
    }
};
