# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        if head.next == None:
            head = None
            return head
        
        l = 0
        temp = head
        
        while temp.next != None:
            temp = temp.next                    #finding length
            l = l + 1
          
        l = l + 1
        del_ind = l-n
        
        
        
     
        if del_ind == 0:
            head = head.next
            
        else:
            i = 0
            t = head
            while i < del_ind-1:
                t = t.next
                i = i + 1
                
            t.next = t.next.next
        
        return head
