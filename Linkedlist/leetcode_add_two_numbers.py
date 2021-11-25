""" You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself """

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        sumi = 0
        string = ""
        string1 = ""
        string2 = ""
        
        s1 = 0 
        s2 = 0
        
        t1 = l1
        while t1 != None:
            string1 = string1 + str(t1.val)
            t1 = t1.next
            
        t2 = l2
        while t2 != None:
            string2 = string2 + str(t2.val)
            t2 = t2.next
            
        string1 = string1[::-1]
        string2 = string2[::-1]
        
        string = str(int(string1) + int(string2))
        
        string  = list(map(int,string[::-1]))
        
        t3 = ListNode(string[0])
        temp = t3
        t3.next = temp
        
        for i in range(len(string)):
            temp.next = ListNode(string[i])
            temp = temp.next
            
        return t3.next
            

