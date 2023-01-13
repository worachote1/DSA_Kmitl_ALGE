# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def mergeBinaryTrees(tree1, tree2):
    # Write your code here.
    if(tree1==None and tree2==None):
        return None
    elif(tree1==None):
        return tree2
    elif(tree2==None):
        return tree1
    tree1.value += tree2.value
    tree1.left,tree1.right = mergeBinaryTrees(tree1.left,tree2.left),mergeBinaryTrees(tree1.right,tree2.right)
    return tree1

