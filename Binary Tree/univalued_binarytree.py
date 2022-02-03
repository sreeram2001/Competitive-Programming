# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        
        def traverse(root):
            if root:
                if root.left:
                    traverse(root.left)
                
                arr.append(root.val)
                
                if root.right:
                    traverse(root.right)
        
        arr = []
        traverse(root)
        
        for i in range(len(arr)-1):
            if arr[i] != arr[i+1]:
                return False
            
        return True
