# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        q = []
        q.append(root)
        arr = []
        
        while q:
           
            level = []
            for i in range(len(q)):
                node = q.pop(0)
                
                if node != None:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
                
                print(level)
                    
            if level != None:
                arr.append(level)
                
        
        arr.reverse()
        if arr:
            arr.pop(0)
        return arr
        
