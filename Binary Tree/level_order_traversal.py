# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        def bfs(root,arr):
            
            if root == None:
                return None
            
            q = []
            q.append(root)
            
            while q:
                level = []
                for i in range(len(q)):
                    root = q.pop(0)
                    if root != None:
                        level.append(root.val)
                        q.append(root.left)
                        q.append(root.right)
                    
                if level != None:
                    arr.append(level)
                    
        arr = []
        bfs(root,arr)
        
        if arr:
            arr.pop()
            
        return arr
                
            
