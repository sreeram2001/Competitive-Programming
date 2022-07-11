class Solution {
    
private:
    
    void dfs(TreeNode* root, vector<int> &arr)
    {
        if(root != NULL) 
        {
            
            if(root->left != NULL)
            {
                dfs(root->left,arr);
            }
            
            arr.push_back(root->val);
            
            if(root->right != NULL) 
            {
                dfs(root->right,arr);
            }
        }
        
        else if(root == NULL)
        {
            return;
        }
    }
    
    
public:

    bool isValidBST(TreeNode* root) {
        vector<int> arr;
        dfs(root,arr);
        
        if(arr.size() <= 1)
        {
            return true;
        }
        
        for(int i=1;i<arr.size();i++)
        {
            if(arr[i-1] >= arr[i])
            {
                return false;
            }
        }
        
        return true;
        
    }
};
