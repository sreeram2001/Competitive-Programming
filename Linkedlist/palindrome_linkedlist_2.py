# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        if head.next == None:
            return True
        
        #slow-fast approach
        fast = slow = head
        
        #middle-node
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        
        #reverse-second-half-list
        curr = slow
        prev = None
        nxt = curr.next
        
        while nxt != None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        curr = prev
  
        
        #check 1st half and 2nd half
        while head != None:
            
            if head.val != curr.val:
                return False
            curr = curr.next
            head = head.next
        
        return True
        
