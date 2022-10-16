
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
