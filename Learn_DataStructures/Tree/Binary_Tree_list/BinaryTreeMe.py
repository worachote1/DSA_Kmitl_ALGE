
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


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

# root node -> left subtree -> right subtree
def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

# left subtree -> root node -> right subtree
def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)

# left subtree -> right subtree -> root node
def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

# display each sub tree in the same hight
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

# search method
def searchBT(rootNode, nodeValue):
    if(not rootNode):
        return "The BT does not exist"

    prn = Queue()
    prn.Enqueue(rootNode)
    while(not prn.isEmpty()):
        q = prn.Dequeue()
        if(q.data == nodeValue):
            return "find this nodeValue !!"
        if(q.leftChild != None):
            prn.Enqueue(q.leftChild)
        if(q.rightChild != None):
            prn.Enqueue(q.rightChild)

    return "doesn't exist"

#insert method
def insert(rootNode,newNode):
    if(not rootNode):
        rootNode = newNode
        return
    
    prn = Queue()
    prn.Enqueue(rootNode)
    while(not prn.isEmpty()):
        q = prn.Dequeue()
        if(q.leftChild == None):
            q.leftChild = newNode
            return
        else:
            prn.Enqueue(q.leftChild)
        if(q.rightChild == None):
            q.rightChild = newNode
            return
        else:
            prn.Enqueue(q.rightChild)
            

#delete node section : find deepest 
# -> move deepest 
# and pasted instaed of the node that wanted to deleted

#find deepest node
def getDeepsNode(rootNode):
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
        deepest_node = q
    return deepest_node

def deleteDeepestNode(rootNode,dNode):
    if(not rootNode):
        return
    prn = Queue()
    prn.Enqueue(rootNode)    
    while(not prn.isEmpty()):
        q = prn.Dequeue()
        if(q.data == dNode.data):
            q=None
        
        if(q.rightChild != None):
            if(q.rightChild.data == dNode.data):
                q.rightChild = None
                return
            prn.Enqueue(q.rightChild)

        if(q.leftChild != None):
            if(q.leftChild.data == dNode.data):
                q.leftChild = None
                return
            prn.Enqueue(q.leftChild)

def deleteNode(rootNode,node):
    if(not rootNode):
        return  

    prn = Queue()
    prn.Enqueue(rootNode)    
    while(not prn.isEmpty()):
        q = prn.Dequeue()
        if(q.data==node.data):
            deepest_node = getDeepsNode(rootNode)
            deleteDeepestNode(rootNode,deepest_node)
            q.data = deepest_node.data
            return
      
        if(q.rightChild != None):
            prn.Enqueue(q.rightChild) 
        if(q.leftChild != None):
            prn.Enqueue(q.leftChild)

newBT = TreeNode("Drinks")
leftChild = TreeNode("Hot")
rightChild = TreeNode("Cold")

tea = TreeNode("Tea")
coffee = TreeNode("Coffee")

leftChild.leftChild = tea
leftChild.rightChild = coffee

newBT.leftChild = leftChild
newBT.rightChild = rightChild

print("--- pre order ---")
preOrderTraversal(newBT)
print("--- in order ---")
inOrderTraversal(newBT)
print("--- post order ---")
postOrderTraversal(newBT)
print("--- level order ---")
levelOrderTraversal(newBT)
print("-------------------")

print(searchBT(newBT,"Coffee"))
# print("--- inserting newNode ---")
# newNode = TreeNode("Cola")
# insert(newBT,newNode)
# preOrderTraversal(newBT)

print("--- deleting newNode ---")
#print(getDeepsNode(newBT).data)
# deleteDeepestNode(newBT,getDeepsNode(newBT))
deleteNode(newBT,TreeNode("Cold"))
levelOrderTraversal(newBT)