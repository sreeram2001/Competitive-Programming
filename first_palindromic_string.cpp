class Solution {
public:
    string firstPalindrome(vector<string>& words) {
        string front, rev;
        
        for(int i=0; i<words.size(); i++)
        {
            front = words[i];
            rev = front;
            
            reverse(rev.begin(), rev.end());
            
            if(front == rev)
            {
                return front;
            }
        }
        return "";
    }
};
