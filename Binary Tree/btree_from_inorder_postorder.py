# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        
        def btree(l,r):
            nonlocal p_ind
            
            if l > r:
                return None

            value = postorder[p_ind]
            root = TreeNode(value)
            p_ind = p_ind - 1
            
            in_ind = inorder.index(value)
            
            root.right = btree(in_ind+1,r)
            root.left = btree(l,in_ind-1)
            
            return root
        
        
        p_ind = len(postorder)-1
        return btree(0,len(postorder)-1)
