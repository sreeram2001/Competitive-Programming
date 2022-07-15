# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(root1,root2):
                        
            if root1 == None:
                return root2
            
            if root2 == None:
                return root1
            
            root1.val = root1.val + root2.val
            
            root1.left = dfs(root1.left,root2.left)
            root1.right = dfs(root1.right,root2.right)
            return root1
            

        root1 = dfs(root1,root2)
        return root1

            

        
