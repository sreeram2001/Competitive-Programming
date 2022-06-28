class Solution {
public:
    int countSubstrings(string s) {
        
        int count = 0;
        
        for(int i=0;i<s.size();i++)
        {
            //for odd length palindromes
            int l=i,r=i;
            
            while(l>=0 && r<s.size() && s[l]==s[r])
            {
                count = count + 1;
                l = l - 1;
                r = r + 1;
            }
            
            //for even length palindromes
            l=i;
            r=i+1;
            
            while(l >= 0 && r<s.size() && s[l]==s[r])
            {
                count = count + 1;
                l = l - 1;
                r = r + 1;
            }
            
        }
        
        return count;      
    }
};
