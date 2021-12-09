# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if head.next == None:
            return head
        
        l = 0
        temp1 = head
        
        while temp1.next != None:
            
            if l==k-1:
                front_node = temp1 
            temp1 = temp1.next
            l = l + 1
            
        l = l + 1
        

        temp2 = head
        i = 0
        l = l - k
        
        if l==0:
            front_node = temp2
            
            while temp2.next != None:
                temp2 = temp2.next
                i = i + 1           
            back_node = temp2
            
            
        else:
            while i < l:
                temp2 = temp2.next
                i = i + 1
            
            back_node = temp2
        
        
        back_node.val, front_node.val = front_node.val, back_node.val
        return head
