"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        dp = []
        
        if root == None:
            return dp

        def preorder(root):
            
            if root:
                dp.append(root.val)
                
            if root.children:
                for i in root.children:
                    preorder(i)
                    
        preorder(root)
        return dp
        
