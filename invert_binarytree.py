
class BinarySarchTree:
    
    #initialise
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
        
    #insertion 
    def insertion(self,data):
        if self.data is None:
            self.data = data
        else:
            if data < self.data:
                if self.left:
                    self.left.insertion(data)
                else:
                    self.left = BinarySarchTree(data)
                    
            if data > self.data:
                if self.right:
                    self.right.insertion(data)
                else:
                    self.right = BinarySarchTree(data)
    
                    
                    
    #inorder - left-root-right
    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.data,end=" ")
        if self.right:
            self.right.inorder()
        

            
    def invert(self):
        if self.left:
            swap(self.left)
        if self.right:
            swap(self.right)
        if self:
            swap(self)
        
        
def swap(node):
    if node.left != None and node.right != None:
        tempo = node.left
        node.left = node.right
        node.right = tempo
            
    elif node.left != None and node.right == None:
        node.right = node.left
        node.left =  None
            
    elif node.right != None and node.left == None:
        node.left = node.right
        node.right = None
            


#DRIVER-CODE
bst = BinarySarchTree(4)
bst.insertion(2)
bst.insertion(1)
bst.insertion(3)
bst.insertion(7)
bst.insertion(6)
bst.insertion(8)

bst.inorder()
print()
bst.invert()
bst.inorder()
            
        