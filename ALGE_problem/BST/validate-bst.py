class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    # Write your code here.
    return helper(tree,float('-inf'),float('inf'))


def helper(root : BST,minVal,maxVal):
    if(root == None):
        return True
    if(not(root.value > minVal and root.value < maxVal)):
        return False
    
    return helper(root.left,minVal,root.value) and helper(root.right,root.value,maxVal)