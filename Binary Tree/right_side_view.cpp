/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<int> rightSideView(TreeNode* root) {
        
        vector<int> dummy;
        if(root==NULL)
        {
            return dummy;
        }
        
        vector<TreeNode*> q;
        vector<int> op;
        q.push_back(root);
        
        while(!q.empty())
        {
            int l = q.size();
            while(l)
            {
                l = l - 1;
                TreeNode* node = q.front();
                q.erase(q.begin());
                
                if(l==0)
                {
                    op.push_back(node->val);
                }
                
                if(node->left)
                {
                    q.push_back(node->left);
                }
                
                if(node->right)
                {
                    q.push_back(node->right);
                }
            }
        }
        
        return op;
        
    }
};
