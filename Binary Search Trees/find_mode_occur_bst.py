# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        dict = {}
        
        def dfs(root):
            if root:
                if root.left:
                    dfs(root.left)
                
                if root.val not in dict:
                    dict[root.val] = 1
                else:
                    dict[root.val] = dict[root.val] + 1
                    
                if root.right:
                    dfs(root.right)
        
        dfs(root)
        
        maxi = max(dict.values())
        modes = []
        
        for i in dict:
            if dict[i] == maxi:
                modes.append(i)
                
        return modes
  
 
        
