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

    def insert(self, val):  
        if(self.root == None):
            self.root = Node(val)
            return self.root
        cur = self.root
        while(True):
            if(val <= cur.data):
                if(cur.left == None):
                    cur.left = Node(val)
                    break
                else:
                    cur = cur.left
            elif(val > cur.data):
                if(cur.right == None):
                    cur.right = Node(val)
                    break
                else:
                    cur = cur.right
        return self.root

    def delete(self,r : Node, val : int):
        #code here
        if(r==None):
            print("Error! Not Found DATA")
        else:
            if(val < r.data):
                r.left = self.delete(r.left,val)
            elif(val > r.data):
                r.right = self.delete(r.right,val)
            
            #found
            else:
                #have one or no child
                if(r.left == None):
                    temp = r.right
                    r = None
                    return temp
                elif(r.right == None):
                    temp = r.left
                    r = None
                    return temp
                #have two children
                else:
                    minHeight_node = self.getMinHeight_node(r.right)
                    r.data = minHeight_node.data
                    r.right = self.delete(r.right,minHeight_node.data)
        return r

    def getMinHeight_node(self,rootNode : Node):
        cur = rootNode
        while(cur.left != None):
            cur = cur.left
        return cur
        
                
def printTree90(node, level = 0):

    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)


tree = BinarySearchTree()
data = input("Enter Input : ").split(",")
#code here

for item in data:

    order = item.split(" ")[0]
    val = item.split(" ")[1]
    if(order == "i"):
        print("insert "+str(val))
        tree.root = tree.insert(int(val))
    elif(order == "d"):
        print("delete "+str(val))
        tree.root = tree.delete(tree.root,int(val))

    printTree90(tree.root)