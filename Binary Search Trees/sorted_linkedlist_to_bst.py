# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        
        
        #find-middle-node
        def middle_node(node):
            
            slow = head
            fast = head
            prev = None
            
            while fast != None and fast.next != None:
                fast = fast.next.next
                prev = slow
                slow = slow.next
                
            if prev != None:
                prev.next = None
            return slow
        
        
        #if NULL
        if head == None:
            return None
        
        mid = middle_node(head)
        root = TreeNode(mid.val)    
        
        #only-one-node
        if root.val == head.val:
            return root
        
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(mid.next)
        return root
            
        
        
