class Solution {
public:
    bool isAnagram(string s, string t) {
        
        map<char, int> mp1;
        map<char, int> mp2;
        string ss ;
        
        //map for string 1
        for(int i=0;i<s.size();i++)
        {
            mp1[s[i]]++;
        }
        
        //map for string 2
        for(int j=0;j<t.size();j++)
        {
            mp2[t[j]]++;
        }
        
        //string with max length
        int maxi = max(s.size(),t.size());
        if(maxi == s.size())
        {
            ss = s;
        }
        else
        {
            ss = t;
        }
        
        for(int ii=0;ii<ss.size();ii++)
        {
            if( !(mp1.count(ss[ii]) || !(mp2.count(ss[ii]))))
               {
                   return false;
               }
            
            else if(mp1[ss[ii]] != mp2[ss[ii]])
            {
                return false;
            }
        }             
        return true;
    }
};
