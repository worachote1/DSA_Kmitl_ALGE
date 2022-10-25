class Node:
    def __init__(self, data):
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
        return self.root
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
#10 4 20 1 5
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)

T.printTree(root)
