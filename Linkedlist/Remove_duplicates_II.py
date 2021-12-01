# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head == None or head.next == None:
            return head
        
        node = ListNode(0,head)
        llist = node
        temp = head
        
        while temp and temp.next:
            while temp.next and temp.val == temp.next.val:
                temp = temp.next
                
            if llist.next == temp:
                llist = llist.next
                
            else:
                llist.next = temp.next
                
                
            temp = temp.next
            
        return node.next
  
