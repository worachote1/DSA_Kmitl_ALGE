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
        print("not balance --> rotate")
        return rightRotate(rootNode)
    #Left Right condition
    if(balance > 1 and  val > rootNode.leftChild.data):
        print("not balance --> rotate")
        rootNode.leftChild = leftRotate(rootNode.leftChild)
        return rightRotate(rootNode)
    #Right Right condition
    if(balance < -1 and val > rootNode.rightChild.data):
        print("not balance --> rotate")
        return leftRotate(rootNode)
    #Right Left condition
    if(balance < -1 and val < rootNode.rightChild.data):
        print("not balance --> rotate")
        rootNode.rightChild = rightRotate(rootNode.rightChild)
        return leftRotate(rootNode)
    
    return rootNode

# End Insert Section .....

# Delete Section
# Delete a node from AVL Tree
# Case I : Tree does;nt exist
# Case II : Rotation is not required 
# Case III : Rotation is required (just like Insert Section)
#         -> LL : left left condition   ->>> Right rotation
#         -> LR : left right condition  ->>> 1.Left rotation 2.Right rotation
#         -> RR : right right condition ->>> Left rotation
#         -> RL : right left condition  ->>> 1.Right rotation 2.Left rotation

def getMinValueNode(rootNode : AVLNode):
    if(rootNode == None or rootNode.leftChild == None):
        return rootNode
    return getMinValueNode(rootNode.leftChild)

def deleteNode(rootNode : AVLNode , val : int):
    if(rootNode == None):
        return rootNode
    elif(val < rootNode.data):
        rootNode.leftChild = deleteNode(rootNode.leftChild,val)
    elif(val > rootNode.data):
        rootNode.rightChild = deleteNode(rootNode.rightChild,val)
    else:
        # node to be deleted have one child or not have any children
        if(rootNode.leftChild == None):
            temp = rootNode.rightChild
            rootNode = None
            return temp
        elif(rootNode.rightChild == None):
            temp = rootNode.leftChild
            rootNode = None
            return temp

        # node to be deleted have two children
        temp = getMinValueNode(rootNode.rightChild) 
        rootNode.data = temp.data
        rootNode.rightChild = deleteNode(rootNode.rightChild,temp.data)

    rootNode.height = 1+max(getHeight(rootNode.leftChild),getHeight(rootNode.rightChild))
    balance = getBalance(rootNode)
    #Left Left condition
    if(balance > 1 and getBalance(rootNode.leftChild) >= 0):
        return rightRotate(rootNode)
    #Right Right condition
    if(balance < -1 and getBalance(rootNode.rightChild) <= 0):
        return leftRotate(rootNode)
    #Left Right condition
    if(balance > 1 and getBalance(rootNode.leftChild) < 0):
        rootNode.leftChild = leftRotate(rootNode.leftChild)
        return rightRotate(rootNode)
    #Right Left condition
    if(balance < -1 and getBalance(rootNode.rightChild) > 0):
        rootNode.rightChild = rightRotate(rootNode.rightChild)
        return leftRotate(rootNode)

    return rootNode
# End Delete section

# print tree method from KMITL
def printTree90(node : AVLNode, level=0):
    if node != None:
        printTree90(node.rightChild, level + 1)
        print('     ' * level, node.data)
        printTree90(node.leftChild, level + 1)

newAVL = AVLNode(5)
newAVL = insertNode(newAVL,10)
newAVL = insertNode(newAVL,15)
newAVL = insertNode(newAVL,20)
newAVL = deleteNode(newAVL,5)
printTree90(newAVL)