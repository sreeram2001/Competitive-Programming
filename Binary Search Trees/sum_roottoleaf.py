# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        if root == None:
            return 0
        
        op = []
        
        def roottoleaf(root,sumi):
            if root == None:
                return
            
            sumi = sumi + [str(root.val)]
            
            if root.left == None and root.right == None:
                op.append(int("".join(sumi)))
                
            roottoleaf(root.left,sumi)
            roottoleaf(root.right,sumi)
            
            
        roottoleaf(root,[])
        
        return sum(op)
            
            
            
        
