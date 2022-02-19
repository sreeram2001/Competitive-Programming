# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        #subroots to list
        def inorder(root):
            
            if root != None:
                inorder(root.left)
                if root.val == subRoot.val:
                    nodes.append(root)
                inorder(root.right)           
            else:
                return 
        

        #check-each-root
        def checknodes(rnodes,sub_rnodes):
            
            if rnodes == None and sub_rnodes == None:
                return True
            
            elif rnodes == None and sub_rnodes != None:
                return False
            
            elif rnodes != None and sub_rnodes == None:
                return False
            
            elif rnodes.val != sub_rnodes.val:
                return False
            
            return checknodes(rnodes.left,sub_rnodes.left) and checknodes(rnodes.right,sub_rnodes.right)
            
          
        nodes = []
        inorder(root)  
        
        for i in nodes:
            if checknodes(i,subRoot):
                return True
        return False
        
                
        
        
