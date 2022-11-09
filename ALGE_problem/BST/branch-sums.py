# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root : BinaryTree):
    # Write your code here.
    res = []
    helper(root,0,res)
    return res

def helper(root : BinaryTree,sumNum : int,res : list):
    
    if(root==None):
        return
    sumNum += root.value
    #it's leaf node
    if(root.left==None and root.right == None):
        res.append(sumNum)
        return
    helper(root.left,sumNum,res)
    helper(root.right,sumNum,res)