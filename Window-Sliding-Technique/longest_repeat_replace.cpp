class Solution {
public:
    int characterReplacement(string s, int k) {
        
        int left=0, repeat=0, max_l=0;
        map<char,int> dict;
        
        for(int i=0;i<s.size();i++)
        {
            dict[s[i]]++;
            
            repeat = max(repeat,dict[s[i]]);
            
            if(i - left - repeat > k - 1)
            {
                dict[s[left]] = dict[s[left]] - 1;
                left = left + 1;
            }
            
            max_l = max(max_l, i-left+1);
        }
        
        return max_l;
    }
};
