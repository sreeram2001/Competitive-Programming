# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        def trees_path(root,path):
            
            if root == None:
                return
            
            if path == "":
                path = path + str(root.val)
            else:
                path = path + "->" + str(root.val)
            
            if root.left == None and root.right == None:
                op.append(path)
                
            
            trees_path(root.left,path)
            trees_path(root.right,path)
            
        
        op = []
        trees_path(root,"")
        return op
        

