class Node:
    def __init__(self, data): 
        self.data = data  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.data) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.data:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.data:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break
                
def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)

def father(r : Node,data):
    #code here
    if(r.data == data):
        return "None Because {0} is Root".format(data)
    cur = r
    while(True):
        if(data <= cur.data):
            if(cur.left == None):
                break
            if(cur.left.data == data):
                return str(cur.data)
            else:   
                cur = cur.left
        elif(data > cur.data):
            if(cur.right == None):
                break
            if(cur.right.data == data):
                return str(cur.data)
            else:
                cur = cur.right
    return "Not Found Data"

tree = BinarySearchTree()
data = input("Enter Input : ").split("/")
for e in data[0].split():
    tree.create(e)
printTree90(tree.root)
print(father(tree.root,data[1]))