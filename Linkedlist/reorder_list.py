# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        if head.next == None:
            return head
        
        arr = []
        re = []
        
        temp = head
        while temp != None:
            arr.append(temp.val)
            temp = temp.next
            
        for i in range(len(arr)//2):
            re.append(arr[i])
            re.append(arr[len(arr)-i-1])
            
        if len(arr)%2 != 0:
            re.append(arr[(len(arr)//2)])

            
        t = head
        i = 0
        while t != None:
            t.val = re[i]
            t = t.next
            i = i + 1
            
            
        return head
