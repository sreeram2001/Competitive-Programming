class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        
        for(int i=0;i<matrix.size();i++)
        {
            for(int j=0;j<matrix.size();j++)
            {
                if(j>i)
                {
                    swap(matrix[i][j],matrix[j][i]);
                }
            }
        }
        
        
        for(int i=0;i<matrix.size();i++)
        {
            int left = 0, right = matrix.size()-1;
            
            while(left < right)
            {
                swap(matrix[i][left],matrix[i][right]);
                left = left + 1;
                right = right - 1;
            }
        }
        
    }
};
