# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        
        
        def check_mirror(l,r):
            if l == None and r == None:
                return True
        
            elif l != None and r == None:
                return False
            
            elif l == None and r != None:
                return False
        
            elif l.val != r.val:
                return False
        
            return (check_mirror(l.left,r.right) and check_mirror(l.right,r.left))
        
        
        return check_mirror(root.left,root.right)
    
