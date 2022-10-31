# This is the class of the input tree. Do not edit.

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def findClosestValueInBst(tree : BST, target):
    # Write your code here.
    return helper(tree,target,float('inf'))

def helper(root : BST,target,closet_val):
    if(root == None):
        return closet_val

    if(abs(target-root.value) < abs(target-closet_val)):
        closet_val = root.value
    
    if(root.value < target):
        closet_val = helper(root.right,target,closet_val)
    elif(root.value > target):
        closet_val = helper(root.left,target,closet_val)
    
    elif(root.value == target):
        return root.value

    return  closet_val 


