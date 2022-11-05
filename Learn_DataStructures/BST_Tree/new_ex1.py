#in the left sub-tree value of a node 
# is less than or equal to its parent node's value.

#in the right sub-tree the value of a node 
# is greater than its parent node's value

class Queue:
    def __init__(self):
        self.q = []
    
    def __str__(self):
        return "".join(str(self.q))
    
    def isEmpty(self):
        return len(self.q)==0
    def Enqueue(self,data):
        self.q.append(int(data))
    def Dequeue(self):
        if(self.isEmpty()):
            return
        self.q.pop(0)

class Node:
    def __init__(self,data):
        self.data = int(data)
        self.leftChild = None
        self.rightChild = None
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None
        
    def insert(self,data):
        if(self.root == None):
            self.root = Node(data)
            return
        
        cur = self.root
        while(True):
            if(data <= cur.data):
                if(cur.leftChild == None):
                    cur.leftChild = Node(data)
                    return
                cur = cur.leftChild
                continue
            if(data > cur.data):
                if(cur.rightChild == None):
                    cur.rightChild = Node(data)
                    return
                cur = cur.rightChild
                continue             

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.rightChild, level + 1)
            print('     ' * level,node)
            self.printTree(node.leftChild, level + 1)


prn = BST()
inp = [int(i) for i in input("Enter Input : ").split()]
for item in inp:
    prn.insert(item)

root = prn.root
prn.printTree(root)
