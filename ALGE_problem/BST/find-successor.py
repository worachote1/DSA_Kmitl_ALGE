class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

def getAll(tree,tree_arr):
    if(tree==None):
        return
    getAll(tree.left,tree_arr)
    tree_arr.append(tree.value)
    getAll(tree.right,tree_arr)
    return tree_arr

def findSuccessor(tree, node):

    prn_data =getAll(tree,[])
    if(prn_data[-1]==node):
        return None
    for i in range(0,len(prn_data)-1):
        if(prn_data[i]==node):
            return prn_data[i+1] 