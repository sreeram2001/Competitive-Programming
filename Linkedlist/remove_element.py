# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        temp = None
        
        while head != None:
            
            if temp == None and head.val != val:
                temp = head
                
            elif head.next != None and head.next.val == val:
                head.next = head.next.next
                
            else:
                head = head.next
                
        return temp
            
