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
            if(data <= cur.data):
                if(cur.left == None):
                    cur.left = Node(data)
                    break
                else:
                    cur = cur.left
            elif(data > cur.data):
                if(cur.right == None):
                    cur.right = Node(data)
                    break
                else:
                    cur = cur.right
        return self.root

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

def find_height(rootNode : Node,h : int):
    if(rootNode == None):
        return h-1
    left_h = find_height(rootNode.left,h+1)
    right_h = find_height(rootNode.right,h+1)
    return max(left_h,right_h)

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)

print("Height of this tree is : "+str(find_height(T.root,0)))