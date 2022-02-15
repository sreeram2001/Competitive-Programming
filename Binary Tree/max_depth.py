# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if root == None:
            return 0
        
        def dfs(root):
            
            if root == None:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            
            return 1+max(left,right)
        
        
        p = dfs(root)
        return p
