# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        self.nodes = []
        
        def inorder(root):
            if root:
                
                inorder(root.left)
                self.nodes.append(root)
                inorder(root.right)
                
            return
                
                
        inorder(root)
        
        self.node_values = [node.val for node in self.nodes]
        self.node_values.sort()
        
        for i in range(len(self.nodes)):
            self.nodes[i].val = self.node_values[i]
            
        
        
