class Queue:
    def __init__(self):
        self.q = []
    def Enqueue(self,i):
        self.q.append(i)
    def Dequeue(self):
        if(len(self.q)==0):
            return ""
        return self.q.pop(0)
    def isEmpty(self):
        return len(self.q) == 0
    def size(self):
        return len(self.q)
    def show(self):
        return self.q.copy()

class TreeNode:
    def __init__(self,data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
    
#root node -> left subtree -> right subtree
def preOrderTraversal(rootNode):
    if not rootNode :
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

#left subtree -> root node -> right subtree
def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)

#left subtree -> right subtree -> root node
def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

# display each sub tree in the same hight
def levelOrderTraversal(rootNode):
    prn = Queue()
    prn.Enqueue(rootNode)
    while(not prn.isEmpty()):
        q = prn.Dequeue()
        if(q.leftChild != None):
            prn.Enqueue(q.leftChild)
        if(q.rightChild != None):
            prn.Enqueue(q.rightChild)
        print(q.data)

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