# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None:
            return False
        
        op = []
        
        def roottoleaf(root,target,sumi):
            if root == None:
                return
            
            sumi = sumi + [root.val]
            
            if root.left == None and root.right == None and sum(sumi)==target:
                op.append(sumi)
                return
            
            roottoleaf(root.left,target,sumi)
            roottoleaf(root.right,target,sumi)

        
        roottoleaf(root,targetSum,[])
        if op:
            return True
        else:
            return False
    
    
            
            
            

            
