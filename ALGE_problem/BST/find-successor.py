# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def findSuccessor(tree, node):
    # Write your code here.
    res = []
    helper(tree,res)
    if(res==[]):
        return None
    for i in range(len(res)):
        if(res[i]==node):
            if(i==len(res)-1):
                return None
            return res[i+1]    

def helper(roootNode : BinaryTree,res : list):
    if(roootNode == None):
        return
    helper(roootNode.left,res)
    res.append(roootNode)
    helper(roootNode.right,res)

