# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def invertBinaryTree(tree : BinaryTree):
    # Write your code here.
    helper(tree)

def helper(tree : BinaryTree):
    if(tree == None):
        return
    if(tree.left == None and tree.right == None):
        return
    temp = tree.right
    tree.right = tree.left
    tree.left = temp

    helper(tree.left)
    helper(tree.right)
