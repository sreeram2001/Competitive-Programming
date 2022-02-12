# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        
        def tree_paths(root,path):
            if root == None:
                return
            
            path = path + [root.val]
            
            if root.left == None and root.right == None and sum(path) == targetSum:
                op.append(path)
                
            
            tree_paths(root.left,path)
            tree_paths(root.right,path)
            
            
        op = []
        tree_paths(root,[])
        return op
        
