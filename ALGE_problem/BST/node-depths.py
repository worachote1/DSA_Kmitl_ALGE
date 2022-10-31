#write a function that takes in a Binary tree
#and return the sum of it's nodes'depths.

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def nodeDepths(root : BinaryTree):
    
    return helper(root,0)

def helper(root : BinaryTree,d):
    if(root == None):
        return 0 
    
    return d + helper(root.left,d+1) +helper(root.right,d+1)

