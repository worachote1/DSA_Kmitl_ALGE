
from typing import List

def inOrderTraverse(tree, array: List):
    # Write your code here.
    if(tree == None):
        return

    inOrderTraverse(tree.left,array)
    array.append(tree.value)
    inOrderTraverse(tree.right,array)
    return array

def preOrderTraverse(tree, array : List):
    # Write your code here.
    if(tree == None):
        return
    array.append(tree.value)
    preOrderTraverse(tree.left,array)
    preOrderTraverse(tree.right,array)
    return array

def postOrderTraverse(tree, array : List):
    # Write your code here.
    if(tree == None):
        return
    postOrderTraverse(tree.left,array)
    postOrderTraverse(tree.right,array)
    array.append(tree.value)
    return array