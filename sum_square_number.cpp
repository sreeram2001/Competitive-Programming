class Solution {
public:
    bool judgeSquareSum(int c) {
        
        long int a = 0;
        long int b = sqrt(c);
        long int res;
        
        while(a<=b)
        {
            res = (a*a) + (b*b);
            
            if(res == c)
            {
                return true;
            }
            
            else if(res > c)
            {
                b = b - 1;
            }
            
            else
            {
                a = a + 1;
            }
        }
        
        return false;
        
    }
};
