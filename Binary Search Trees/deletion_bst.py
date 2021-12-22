# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root == None:
            return root
        
        parent = None
        node = root
        
        while node != None and node.val != key:
            parent = node
            
            if key < node.val:
                node = node.left
            else:
                node = node.right
         
        #node not present
        if node == None:
            return root
        
        #case-1 no child
        if node.left == None and node.right == None:
            if root == node:
                root = None
        
            elif node != root:
                if parent.left == node:
                    parent.left = None
                else:
                    parent.right = None
                
                
        #case-2 one child
        elif node.left != None and node.right == None:
            if node == root:
                root = node.left
            else:
                if parent.left == node:
                    parent.left = node.left
                else:
                    parent.right = node.left
                
        elif node.left == None and node.right != None:
            if node == root:
                root = node.right
            else:
                if parent.right == node:
                    parent.right = node.right
                else:
                    parent.left = node.right
                
                
        #case-3 two child present
        else:
            main = node
            node = node.left
            
            while node.right != None:
                node = node.right
                
            
            temp = node.val
            self.deleteNode(root,temp)
            main.val = temp
            

        return root
