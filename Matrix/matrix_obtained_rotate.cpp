class Solution {
public:
    bool findRotation(vector<vector<int>>& mat, vector<vector<int>>& target) {
        
        for(int c=0;c<4;c++)
        {
            if(mat == target)
            {
                return true;
            }
            
            for(int i=0;i<mat.size();i++)
            {
                for(int j=i+1;j<mat.size();j++)
                {
                    swap(mat[i][j],mat[j][i]);
                }
            }
            
            
            for(int i=0;i<mat.size();i++)
            {
                int left=0, right = mat.size()-1;
                
                while(left<right)
                {
                    swap(mat[i][left],mat[i][right]);
                    left = left + 1;
                    right = right - 1;
                }
            }
        }
        
        return false;
    }
};
