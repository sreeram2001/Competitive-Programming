#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow = head
        fast = slow.next
        
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            
        temp1 = head
        temp2 = slow.next
        slow.next = None
        
        curr = temp2
        prev = nxt = None
        
        while curr != None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        temp2 = prev
        
        dummy = ListNode(0)
        curr = dummy
        
        while temp1 != None or temp2 != None:
            if temp1 != None:
                curr.next = temp1
                curr = curr.next
                temp1 = temp1.next
                
            if temp2 != None:
                curr.next = temp2
                curr = curr.next
                temp2 = temp2.next
                
        return dummy.next
