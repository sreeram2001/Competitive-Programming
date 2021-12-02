class Solution {
public:
    int missingNumber(vector<int>& nums) {
        
        int n, missing=-1;
        
        sort(nums.begin(),nums.end());
        
        n = nums[nums.size()-1];
        
        for(int i=0;i<n;i++)
        {
            if(i == nums[i])
            {
                continue;
            }
            
            else
            {
                missing = i;
                return missing;
            }
        }
        
        return n+1;
        
    }
};
