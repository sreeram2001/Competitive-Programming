class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        
        map<int, int>mp;
        int dupli;
        
        for(int i=0;i<nums.size();i++)
        {
            mp[nums[i]]++;
        }
        
        for(auto i:mp)
        {
            if(i.second != 1)
            {
                dupli = i.first;
            }
        }
        return dupli;
    }
};
