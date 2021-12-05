class Solution {
public:
    int countBinarySubstrings(string s) {
        
        int counter = 0,previous=0,current=1;
        
        for(int i=1;i<s.size();i++)
        {
            if(s[i] == s[i-1])
            {
                current = current + 1;
            }
            
            else
            {
                counter = min(previous,current) + counter;
                previous = current;
                current = 1;
            }
        }
        
        counter = min(previous,current) + counter;
        return counter;
    }
};
