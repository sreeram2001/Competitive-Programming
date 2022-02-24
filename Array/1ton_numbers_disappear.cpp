class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        
        map<int,int> mp;
        vector<int> arr;
        
        for(int i=1;i<=nums.size();i++)
        {
            mp[i]++;
        }
        
        for(int i=0;i<nums.size();i++)
        {
            mp[nums[i]]++;
        }
        
        for(auto i:mp)
        {
            if(i.second == 1)
            {
                arr.push_back(i.first);
            }
        }
        
        return arr;
    }
};
