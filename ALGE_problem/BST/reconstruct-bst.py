# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def insert(value,root : BST):
    new_node = BST(value)
    cur = root
    while(True):
        if(value <= cur.value):
            if(cur.left == None):
                cur.left = new_node
                return
            cur = cur.left
        elif(value > cur.value):
            if(cur.right == None):
                cur.right = new_node
                return
            cur = cur.right
        

def reconstructBst(preOrderTraversalValues):
    if(preOrderTraversalValues==[]):
        return None
    
    root = BST(preOrderTraversalValues[0])
    for i in range(1,len(preOrderTraversalValues)):
        insert(preOrderTraversalValues[i],root)            
    
    return root
