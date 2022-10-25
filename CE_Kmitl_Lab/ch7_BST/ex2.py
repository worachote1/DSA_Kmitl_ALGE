class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        # Code Here
        if(self.root == None):
            self.root = Node(data)
            return self.root
        
        cur = self.root
        while(True):
            if(data < cur.data):
                if(cur.left==None):
                    cur.left = Node(data)
                    break;
                cur = cur.left
            elif(data>cur.data):
                if(cur.right==None):
                    cur.right = Node(data)
                    break;
                cur = cur.right
        
    
def printTree(node, level = 0):
    if node != None:
        printTree(node.right, level + 1)
        print('     ' * level, node)
        printTree(node.left, level + 1)

def findHeight(rootNode,h):
    if(rootNode == None):
        return h-1
    a = findHeight(rootNode.left,h+1)
    b = findHeight(rootNode.right,h+1)

    return max(a,b)    

inp = [int(i) for i in input("Enter Input : ").split(" ")]
newBST = BST()
for item in inp:
    newBST.insert(item)

#test
# printTree(newBST.root)

print("Height of this tree is : {0}".format(findHeight(newBST.root,0)))