class Solution {
public:
    vector<int> shortestToChar(string s, char c) {
        
        vector<int> ind;
        int left=-10000000;
        
        for(int i=0;i<s.size();i++)
        {
            if(s[i] == c)
            {
                left = i;
            }
            
            ind.push_back(i-left);
        }
        
        left = INT_MAX;
        
        for(int i=s.size()-1;i>-1;i--)
        {
            if(s[i] == c)
            {
                left = i;
            }
            ind[i] = min(ind[i],left-i);
        }
        
        return ind;
        
    }
};
