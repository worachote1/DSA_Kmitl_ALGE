class Queue:
    def __init__(self):
        self.q = []
    def isEmpty(self):
        return len(self.q)==0
    def Enqueue(self,data):
        self.q.append(data)
    def Dequeue(self):
        self.q.pop(0)
    def size(self):
        return len(self.q)
    def getData(self,idx):
        return self.q[idx]
    def coppy(self):
        return self.q.copy()

class AVLNode:
    def __init__(self,data) :
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.height = 1
    
def preOrderTraversal(rootNode : AVLNode):
    if(rootNode == None):
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

def inOrderTraversal(rootNode : AVLNode):
    if(rootNode == None):
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)

def postOrderTraversal(rootNode : AVLNode):
    if(rootNode == None):
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

def levelOrderTraversal(rootNode):
    if(not rootNode):
        return
    prn = Queue()
    prn.Enqueue(rootNode)
    while(not prn.isEmpty()):
        q = prn.Dequeue()
        if(q.leftChild != None):
            prn.Enqueue(q.leftChild)
        if(q.rightChild != None):
            prn.Enqueue(q.rightChild)
        print(q.data)

def searchNode(rootNode : AVLNode,val : int):
    if(rootNode.data == val):
        print("The value is found")
        return
    elif(val < rootNode.data):
        if(rootNode.leftChild.data==val):
            print("The value is found")
            return            
        else:
            searchNode(rootNode.leftChild,val)
    else:
        if(rootNode.rightChild.data==val):
            print("The value is found")
            return            
        else:
            searchNode(rootNode.rightChild,val)      

# Insert Section
# Insert a node in AVL Tree
# Case I : Rotation is not required
# Case II : Rotation is required 
#         -> LL : left left condition   ->>> Right rotation
#         -> LR : left right condition  ->>> 1.Left rotation 2.Right rotation
#         -> RR : right right condition ->>> Left rotation
#         -> RL : right left condition  ->>> 1.Right rotation 2.Left rotation

def getHeight(rootNode:AVLNode):
    if(rootNode==None):
        return 0
    return rootNode.height

def rightRotate(disbalanceNode:AVLNode):
    newRoot = disbalanceNode.leftChild
    disbalanceNode.leftChild = disbalanceNode.leftChild.rightChild
    newRoot.rightChild = disbalanceNode
    #then update the height of newRoot and disbalanceNode
    disbalanceNode.height = 1+max(getHeight(disbalanceNode.leftChild),getHeight(disbalanceNode.rightChild))
    newRoot.height = 1+max(getHeight(newRoot.leftChild),getHeight(newRoot.rightChild))

    return newRoot

def leftRotate(disbalanceNode:AVLNode):
    newRoot = disbalanceNode.rightChild
    disbalanceNode.rightChild = disbalanceNode.rightChild.leftChild
    newRoot.leftChild = disbalanceNode
    #then update the height of newRoot and disbalanceNode
    disbalanceNode.height = 1+max(getHeight(disbalanceNode.leftChild),getHeight(disbalanceNode.rightChild))
    newRoot.height = 1+max(getHeight(newRoot.leftChild),getHeight(newRoot.rightChild))

    return newRoot

def getBalance(rootNode:AVLNode):
    if(rootNode == None):
        return 0
    return getHeight(rootNode.leftChild)-getHeight(rootNode.rightChild)

def insertNode(rootNode:AVLNode,val:int):
    if(rootNode == None):
        return AVLNode(val)
    elif(val < rootNode.data):
        rootNode.leftChild = insertNode(rootNode.leftChild,val)
    else:
        rootNode.rightChild = insertNode(rootNode.rightChild,val)

    rootNode.height = 1+max(getHeight(rootNode.leftChild),getHeight(rootNode.rightChild))
    balance = getBalance(rootNode) #Identify which condition is in Case II 
    #Left Left condition
    if (balance > 1 and val < rootNode.leftChild.data):
        return rightRotate(rootNode)
    #Left Right condition
    if(balance > 1 and  val > rootNode.leftChild.data):
        rootNode.leftChild = leftRotate(rootNode.leftChild)
        return rightRotate(rootNode)
    #Right Right condition
    if(balance < -1 and val > rootNode.rightChild.data):
        return leftRotate(rootNode)
    #Right Left condition
    if(balance < -1 and val < rootNode.rightChild.data):
        rootNode.rightChild = rightRotate(rootNode.rightChild)
        return leftRotate(rootNode)
    
    return rootNode

# End Insert Section .....

# print tree method from KMITL
def printTree90(node, level=0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)
newAVL = AVLNode(10)