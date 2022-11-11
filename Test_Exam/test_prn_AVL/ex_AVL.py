class AVLNode:
    def __init__(self,data) :
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.height = 1


def getHeight(rootNode : AVLNode):
    if(rootNode==None):
        return 0
    return rootNode.height

def getBalance(rootNode:AVLNode):
    if(rootNode == None):
        return 0
    return getHeight(rootNode.leftChild)-getHeight(rootNode.rightChild)

def leftRotate(disbal_Node : AVLNode):
    newRoot = disbal_Node.rightChild
    disbal_Node.rightChild = disbal_Node.rightChild.leftChild
    newRoot.left = disbal_Node

    disbal_Node.height = 1+max(getHeight(disbal_Node.leftChild),getHeight(disbal_Node.rightChild))
    newRoot.height = 1+max(getHeight(newRoot.leftChild),getHeight(newRoot.rightChild))
    return newRoot
def rightRotate(disbal_Node : AVLNode):
    newRoot = disbal_Node.leftChild
    disbal_Node.leftChild = disbal_Node.leftChild.rightChild
    newRoot.right = disbal_Node
    
    disbal_Node.height = 1+max(getHeight(disbal_Node.leftChild),getHeight(disbal_Node.rightChild))
    newRoot.height = 1+max(getHeight(newRoot.leftChild),getHeight(newRoot.rightChild))
    return newRoot

def insert(rootNode : AVLNode,val:int):
    if(rootNode==None):
        return AVLNode(val)
    elif(val < rootNode.data):
        rootNode.leftChild = insert(rootNode.leftChild,val)
    else:
        rootNode.rightChild = insert(rootNode.rightChild,val)
    
    rootNode.height  = 1+max(getHeight(rootNode.leftChild),getHeight(rootNode.rightChild))
    balance = getBalance(rootNode)

    #check condition
    #Left Left
    if(balance > 1 and val < rootNode.leftChild.data):
        return rightRotate(rootNode)
    #Left Right
    if(balance > 1 and val > rootNode.leftChild.data):
        rootNode.leftChild = leftRotate(rootNode.leftChild)
        return rightRotate(rootNode)
    
    #Right Right
    if(balance < -1 and val > rootNode.rightChild.data):
        return leftRotate(rootNode)
    #Right Left
    if(balance < -1 and val < rootNode.rightChild.data):
        rootNode.rightChild = rightRotate(rootNode.rightChild)
        return leftRotate(rootNode)
    
    return rootNode

