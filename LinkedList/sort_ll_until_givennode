
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
        
class Linkedlist:
    def __init__(self):
        self.head = None
        
    def insertend(self,data):
        node = Node(data)
        
        if self.head == None:
            self.head = node
            
        else:
            temp = self.head
            
            while temp.next != None:
                temp = temp.next
                
            temp.next = node
            node.next = None
            
            
    def traversal(self):
        temp = self.head
        
        while temp != None:
            print(temp.data)
            temp = temp.next
            
            
    def sorting(self):
        t1 = self.head
        
        while t1.next != None:
            t2 = t1.next
            
            while t2.next != None:
                if t2.data < t1.data:
                    temp = t1.data
                    t1.data = t2.data
                    t2.data = temp
                t2 = t2.next
                
            t1 = t1.next
        
            
            
#user-data
ll = Linkedlist()
ll.insertend(45)
ll.insertend(34)
ll.insertend(67)
ll.insertend(45)
ll.insertend(76)
ll.traversal()
ll.sorting()
print()
ll.traversal()
