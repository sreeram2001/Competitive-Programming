# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head.next == None:
            return head
        
        temp = head
        length = 1
        
        while temp.next != None:
            temp = temp.next
            length = length + 1
        
        
        l = length//2 + 1
        i = 0
        t = head
        
        while i < l-1:
            t = t.next
            i = i + 1
            
        return t
        
