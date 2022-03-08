# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        def bfs(arr,root):
            q = []
            q.append(root)
            c = 0
            
            while q:
                
                level = []
                for i in range(len(q)):
                    node = q.pop(0)
                    
                    if node != None:
                        level.append(node.val)
                        q.append(node.left)
                        q.append(node.right)
                 
                if level != None:
                    if c%2 == 0:
                        arr.append(level)
                    else:
                        arr.append(level[::-1])
                    c = c + 1
           
        
        arr = []
        bfs(arr,root)
        if arr:
            arr.pop()
        
        return arr
        
