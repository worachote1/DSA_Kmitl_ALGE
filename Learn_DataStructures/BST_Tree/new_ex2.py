class Node:
    def __init__(self,data) :
        self.data = int(data)
        self.leftChild = None
        self.rightChild = None
    def __str__(self) :
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self,data):
        if(self.root == None):
            self.root = Node(data)
            return;
        cur = self.root
        while(True):
            if(data <= cur.data):
                if(cur.leftChild==None):
                    cur.leftChild = Node(data)
                    return
                cur = cur.leftChild
                continue
            if(data > cur.data):
                if(cur.rightChild==None):
                    cur.rightChild = Node(data)
                    return
                cur = cur.rightChild
                continue
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.rightChild, level + 1)
            print('     ' * level,node)
            self.printTree(node.leftChild, level + 1)

    def findHeight(self,rootNode,h=0):
        if(rootNode==None):
            return h-1
        left_height = self.findHeight(rootNode.leftChild,h+1)
        right_height = self.findHeight(rootNode.rightChild,h+1)
        return max(left_height,right_height)

prn = BST()
inp = [int(i) for i in input("Enter Input : ").split()]
for item in inp:
    prn.insert(item)

prn.printTree(prn.root)
print("Height of this tree is : ")
print(prn.findHeight(prn.root))