# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
         
        
        def dfs(root,sett):
            if root:
                if root.left:
                    dfs(root.left,sett)
                    
                sett.add(root.val)
                    
                if root.right:
                    dfs(root.right,sett)
                    
            
        sett = set()
        dfs(root,sett)
        
        if len(sett) == 1:
            return -1
        else:
            first = second = 2**31
            for i in sett:
                
                if i < first:
                    second = first
                    first = i
                
                elif i > first and i < second:
                    second = i
                    
                    
            return second
        
        
