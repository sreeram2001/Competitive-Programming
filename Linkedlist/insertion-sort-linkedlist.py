# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head == None:
            return head
        
        if head.next == None:
            return head
        
        temp = head
        
        while temp != None:
            t = head
            
            while temp != t:
                
                if t.val > temp.val:
                
                    t.val, temp.val = temp.val, t.val
                                       
                t = t.next
                
            temp = temp.next
                
        return head
