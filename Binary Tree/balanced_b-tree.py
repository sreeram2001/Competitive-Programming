# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        self.op = True
        
        if root == None:
            return True
        
        def balanced(root):
            if root == None:
                return 0
            
            if self.op == False:
                return 0
          
            left = balanced(root.left)
            right = balanced(root.right)
                
            if abs(left-right)>1:
                self.op = False

            return max(left,right) + 1
        
        balanced(root)
        return self.op
         
        
                
            
