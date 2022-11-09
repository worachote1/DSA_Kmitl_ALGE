class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    

def heightBalancedBinaryTree(tree : BinaryTree):
    # Write your code here.
    return helper(tree)

def helper(tree : BinaryTree):
    if(tree == None):
        return True
    if(tree.left == None and tree.right == None):
        return True
    x = findHeight(tree.left,0)
    y = findHeight(tree.right,0)
    return (abs(x-y)<=1) and helper(tree.left) and helper(tree.right)

def findHeight(tree : BinaryTree,h):
    if(tree == None):
        return h-1
    a = findHeight(tree.left,h+1)
    b = findHeight(tree.right,h+1)

    return max(a,b)