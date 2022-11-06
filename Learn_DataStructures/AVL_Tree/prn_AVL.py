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

# Insert a node in AVL Tree
# Case I : Rotation is not required
# Case II : Rotation is required 
#         -> LL : left left condition
#         -> LR : left right condition
#         -> RR : right right condition
#         -> RL : right left condition

newAVL = AVLNode(10)