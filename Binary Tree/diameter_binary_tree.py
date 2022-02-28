# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        maxi = [0]
        
        if root == None:
            return maxi[0]
        
        def dfs(root):
            if root == None:
                return -1
            
            l = dfs(root.left)
            r = dfs(root.right)
            maxi[0] = max(maxi[0],l+r+2)
            
            return 1 + max(l,r)
        
        
        dfs(root)
        return maxi[0]
