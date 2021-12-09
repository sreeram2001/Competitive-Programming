# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None:
            head = None
            return head
            
        length = 1
        temp = head
        
        while temp.next != None:
            temp = temp.next
            length = length + 1
            
        l = length//2+1
        l = l - 1
        
        i = 0
        t = head
        while i < l-1:
            t = t.next
            i = i + 1
            
        t.next = t.next.next
        
        return head
