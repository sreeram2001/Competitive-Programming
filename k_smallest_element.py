# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        
        self.inorder(root,k,arr)
        return arr[k-1]

   
    def inorder(self,root,k,arr):
        
        if root.left:
            self.inorder(root.left,k,arr)
            
        arr.append(root.val)

        if root.right:
            self.inorder(root.right,k,arr)
            
        return arr

            
