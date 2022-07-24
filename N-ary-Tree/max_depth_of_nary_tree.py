"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        
        if root == None:
            return 0
        
        if root.children == None:
            return 1
        
        count = [0]     #to count level or depth of tree
        arr = []        #stores level order nodes
        
        #using level order traversal or bfs
        def bfs(root):
            
            q = []          #queue to store nodes
            q.append(root)
            
            while q:
                lvl = []        #for each level nodes
                
                for i in range(len(q)):
                    node = q.pop(0)
                    
                    if node != None:
                        lvl.append(node.val)
                        
                        #add all child nodes to queue
                        for n in node.children:
                            q.append(n)
                            
                if len(lvl) > 0:
                    arr.append(lvl)
                    
        bfs(root)       #calling bfs function
        return len(arr)     #len(arr) gives level of tree or depth
                            
