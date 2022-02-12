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
        
        
        def sum_path(root,target,path):

            if root == None:
                return
            
            if root.left == None and root.right == None:
            
                path = path + root.val
                if target == path:
                    return True
                else:
                    return False
            
            if (sum_path(root.left,target,path+root.val) or sum_path(root.right,target,path+root.val)):
                return True
            return False
    
        return sum_path(root,targetSum,0)

                
            
