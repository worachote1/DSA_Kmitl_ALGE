class TreeNode(object): 
    def __init__(self, val): 
        self.val = val 
        self.left = None
        self.right = None
        self.height = 0

    def __str__(self):
        return str(self.val)


class AVL_Tree(object): 
    def __init__(self):
        self.root = None
    
    def rr(self,px):
        py = px.right
        px.right = py.left
        py.left = px
        return py
    
    def ll(self,px):
        py = px.left
        px.left = py.right
        py.right = px
        return py
    
    def changeHeight(self,a):
        if a!=None:
            a.height = max(self.changeHeight(a.left),self.changeHeight(a.right))+1
            return a.height
        else:
            return -1
    
    def insert(self,node,data):
        data = int(data)
        if self.root is None:
            self.root = TreeNode(data)
            return self.root
        else:
            if node != None:
                if data < node.val:
                    node.left = self.insert(node.left,data)
                else:
                    node.right = self.insert(node.right,data)
            else:
                return TreeNode(data)
            
            
            l = node.left.height if node.left is not None else -1
            r = node.right.height if node.right is not None else -1
            if abs(l-r)>1:
                a = self.root
                if l>r:
                    if data<node.left.val:
                        a = self.ll(node)
                    else:
                        node.left = self.rr(node.left)
                        node = self.ll(node)
                        a = node
                else:
                    if data<node.right.val:
                        node.right = self.ll(node.right)
                        node = self.rr(node)
                        a = node
                    else:
                        a = self.rr(node)
                self.changeHeight(a)
                return a
            else:
                node.height = max(l,r)+1
                return node

    #Test prn insert
    def insert_prn(self, data):
        if self.root == None:
            self.root = TreeNode(data)
        else:
            curr = self.root
            while True:
                if data < curr.val:
                    if curr.left == None:
                        curr.left = TreeNode(data)
                        break
                    else:
                        curr = curr.left
                else:
                    if curr.right == None:
                        curr.right = TreeNode(data)
                        break
                    else:
                        curr = curr.right
        return self.root


def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)

#prn_ test method : for checking balance
class TreeInfo :
    def __init__(self,isBalanced,height):
        self.isBalanced = isBalanced
        self.height = height

def heightBalancedBinaryTree(tree):
    # Write your code here.
    treeInfo = getTreeInfo(tree)
    return treeInfo.isBalanced

def getTreeInfo(node):
    if(node == None):
        return TreeInfo(True,-1)
    
    leftSubtreeInfo = getTreeInfo(node.left)
    rightSubtreeInfo = getTreeInfo(node.right)

    isBalanced = leftSubtreeInfo.isBalanced and rightSubtreeInfo.isBalanced and abs(
        leftSubtreeInfo.height-rightSubtreeInfo.height)<=1
    
    height = max(leftSubtreeInfo.height,rightSubtreeInfo.height)+1
    return TreeInfo(isBalanced,height)
    
# Recursive function to clone a binary tree
def cloneBinaryTree(root):
 
    # base case
    if root is None:
        return None
 
    # create a new node with the same data as the root node
    root_copy = TreeNode(root.val)
 
    # clone the left and right subtree
    root_copy.left = cloneBinaryTree(root.left)
    root_copy.right = cloneBinaryTree(root.right)
 
    # return cloned root node
    return root_copy

myTree = AVL_Tree() 
prn_tree = AVL_Tree()
root = None

data = input("Enter Input : ").split()
for e in data:
    print("insert :",e)
    # prn_tree.insert_prn(e)
    temp = cloneBinaryTree(root)
    root = myTree.insert(root, e)
    printTree90(root)

    #test 44 clone temp then insert_prn
    prn_tree= cloneBinaryTree(temp)
    if(temp != None):
        print("prn tre 44 : ")
        printTree90(prn_tree)

        #check balanced for display
        print(heightBalancedBinaryTree(prn_tree))

    print("===============")
    