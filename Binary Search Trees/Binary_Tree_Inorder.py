# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        listt = []
        
        if root:
        
            if root.left:
                listt = listt + self.inorderTraversal(root.left)
            
            listt.append(root.val)
        
            if root.right:
                listt = listt + self.inorderTraversal(root.right)
            
            
        return listt
        
