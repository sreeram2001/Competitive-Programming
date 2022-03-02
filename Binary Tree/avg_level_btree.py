# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        def bfs(root,ele):
            
            if root == None:
                return None
            
            q = []
            q.append(root)
            
            while q:
                lvl = []
                
                for i in range(len(q)):
                    node = q.pop(0)
                    
                    if node:
                        lvl.append(node.val)
                        q.append(node.left)
                        q.append(node.right)
                        
                if lvl:
                    ele.append(lvl)
                    
        ele = []
        op = []
        bfs(root,ele)
        
        for i in ele:
            avg = sum(i)/len(i)
            op.append(avg)
            
        return op
