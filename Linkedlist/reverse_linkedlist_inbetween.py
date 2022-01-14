# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right or head == None:
            return head
        
        curr = head
        prev = None
        
        while left > 1:
            prev = curr
            curr = curr.next
            left = left - 1
            right = right - 1
            
        temp = curr
        node = prev
        
        #reversal
        while right > 0:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            
            right = right - 1
         
        
        if node != None:
            node.next = prev
        else:
            head = prev
        temp.next = curr

        return head
        
        
 
