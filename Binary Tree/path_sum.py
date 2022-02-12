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
        
        def sum_path(root,target,path):

            if root == None:
                return
            
            path = path + [root.val]
            
            if root.left == None and root.right == None and sum(path)==target:
                op.append(path)
                return
            
            sum_path(root.left,target,path)
            sum_path(root.right,target,path)

            
        sum_path(root,targetSum,[])
        
        if op:
            return True
        else:
            return False

