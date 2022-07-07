"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        
        if root == None:
            return None
        
        q = []              #queue
        result = []         #to store the final output
        
        q.append(root)
        
        while q:        #implement when q is not empty
            
            lvl = []            #to store for each level
            
            for i in range(len(q)):
                node = q.pop(0)         #pop element index0, FIFO
                
                if node:
                    lvl.append(node.val)    
                    
                if node.children:               #iterate to each children
                    for c in node.children:
                        q.append(c)
 
                        
            result.append(lvl)
            
        return result
            
