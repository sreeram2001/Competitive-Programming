class Solution {
public:
    int repeatedNTimes(vector<int>& nums) {
        
        int n = nums.size()/2;         //gives the value of n
        map<int,int> mp;            //hashmap to store frequency
        int op;
        
        for(int i=0;i<nums.size();i++)
        {
            mp[nums[i]]++;
        }
        
        //element which appears n times
        for(auto i:mp)
        {
            if(i.second == n)
            {
                op = i.first;
            }
        }
        return op;
    }
};
