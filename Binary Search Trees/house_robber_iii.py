# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root):
            
            if root == None:
                return 0, 0
            
            left, grand_left = dfs(root.left)
            right, grand_right = dfs(root.right)

            root_incl = root.val + grand_left + grand_right
            root_not_incl = max(left,grand_left) + max(right,grand_right)
            
            return root_incl, root_not_incl
        
        return max(dfs(root))
            
            
            
