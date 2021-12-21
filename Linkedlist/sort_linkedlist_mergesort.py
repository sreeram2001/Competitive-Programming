# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    
    def merge(self,l,r):
        node = temp = ListNode(0)
        
        while l != None and r != None:
            
            if l.val < r.val :
                temp.next = l
                l = l.next
            else:
                temp.next = r
                r = r.next
            temp = temp.next
        
        
        if l != None:
            temp.next = l
            
        if r != None:
            temp.next = r
            
        return node.next
            
            
            
    def middle(self,head):
        slow = head
        curr = head.next
        
        while curr != None and curr.next != None:
            curr = curr.next.next
            slow = slow.next
            
        return slow
        
        
    
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head == None or head.next == None:
            return head
        
        mid = self.middle(head)
        l = head
        r = mid.next
        mid.next = None
        
        left = self.sortList(l)
        right = self.sortList(r)
        
        final = self.merge(left,right)
        return final
        
