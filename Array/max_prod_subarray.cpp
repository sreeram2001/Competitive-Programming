class Solution {
public:
    int maxProduct(vector<int>& nums) {
        
        int maxi = 1, mini = 1;
        int maxi_1;
        int op = *max_element(nums.begin(),nums.end());
        
        for(int i=0;i<nums.size();i++)
        {
            maxi_1 = maxi;
            
            maxi = max(max(mini*nums[i],maxi*nums[i]),nums[i]);
            mini = min(min(mini*nums[i],maxi_1*nums[i]),nums[i]);
            
            op = max(maxi,op);
        }
        
        return op;
    }
};
