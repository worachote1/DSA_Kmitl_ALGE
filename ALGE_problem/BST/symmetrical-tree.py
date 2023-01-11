# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def helper(subleft : BinaryTree,subRight : BinaryTree):
    if(subleft == subRight == None):
        return True
    elif(subleft == None or subRight == None):
        return False
    if(subleft.value!=subRight.value):
        return False
    return helper(subleft.left,subRight.right) and helper(subleft.right,subRight.left)

def symmetricalTree(tree : BinaryTree):
    # Write your code here.
    return helper(tree.left,tree.right)