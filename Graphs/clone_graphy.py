"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        clone = {}
        if node == None:
            return None
        
        def dfs(node):
            if node in clone:
                return clone[node]
            
            node_clone = Node(node.val)
            clone[node] = node_clone
            
            for i in node.neighbors:
                node_clone.neighbors.append(dfs(i))
            return node_clone
        
        g = dfs(node)
        return g
    
