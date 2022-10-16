#in the left sub-tree value of a node 
# is less than or equal to its parent node's value.

#in the right sub-tree the value of a node 
# is greater than its parent node's value

class Queue:
    def __init__(self):
        self.q = []

    def Enqueue(self, i):
        self.q.append(i)

    def Dequeue(self):
        if(len(self.q) == 0):
            return ""
        return self.q.pop(0)

    def isEmpty(self):
        return len(self.q) == 0

    def size(self):
        return len(self.q)

    def show(self):
        return self.q.copy()


class BSTNode:
    def __init__(self,data) :
        self.data = data
        self.leftChild = None
        self.rightChild = None

def insertionNode(rootNode,nodeValue):
    if rootNode.data == None:
        rootNode.data = nodeValue
        return
    elif (nodeValue <= rootNode.data):
        if(rootNode.leftChild == None):
            rootNode.leftChild = BSTNode(nodeValue)
        else:
            insertionNode(rootNode.leftChild,nodeValue)
    elif (nodeValue > rootNode.data):
        if(rootNode.rightChild == None):
            rootNode.rightChild = BSTNode(nodeValue)
        else:
            insertionNode(rootNode.rightChild,nodeValue)

    return "Insert success !"

def insertionNode_prn(rootNode,nodeValue):
    if rootNode.data == None:
        rootNode.data = nodeValue
        return
    cur = rootNode
    while(True):
        if(cur.data > nodeValue):
            if(cur.leftChild == None):
                cur.leftChild = BSTNode(nodeValue)
                break;
            else:
                cur = cur.leftChild
        elif(cur.data < nodeValue):
            if(cur.rightChild == None):
                cur.rightChild = BSTNode(nodeValue)
                break;
            else:
                cur = cur.rightChild
        
def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)

def postOrderTraversal(rootNode):
    if not rootNode:
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

#search
def searchNode(rootNode,nodeValue):
    if(rootNode.data==nodeValue):
        return "The Value is found !"
    elif(nodeValue<=rootNode.data):
        if(rootNode.leftChild==None):
            print("Not f")
            return
        if rootNode.leftChild.data == nodeValue:
            print("The value is found")
        else:
            searchNode(rootNode.leftChild,nodeValue)
    elif(nodeValue>rootNode.data):
        if(rootNode.rightChild==None):
            print("Not f")
            return
        if rootNode.rightChild.data == nodeValue:
            print("The value is found")
        else:
            searchNode(rootNode.rightChild,nodeValue)

#delete section
def minValueNode(bstNode):
    current = bstNode
    while(current.left != None):
        current = current.leftChild
    return current

def deleteNode(rootNode,nodeValue):
    if rootNode == None:
        return rootNode

    if (nodeValue < rootNode.data):
        rootNode.leftChild = deleteNode(rootNode.leftChild,nodeValue)
    elif(nodeValue > rootNode.data):
        rootNode.rightChild = deleteNode(rootNode.rightChild,nodeValue)


#delete all
def delete_Alll(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None

#this method from KMITL grader
def printTree90(node, level = 0):
    if node != None:
        printTree90(node.rightChild, level + 1)
        print('     ' * level, node.data)
        printTree90(node.leftChild, level + 1)

newBST = BSTNode(None)

insertionNode_prn(newBST,4)
insertionNode_prn(newBST,3)
insertionNode_prn(newBST,1)
insertionNode_prn(newBST,2)
insertionNode_prn(newBST,7)
insertionNode_prn(newBST,6)
insertionNode_prn(newBST,8)
printTree90(newBST)


# levelOrderTraversal(newBST)

