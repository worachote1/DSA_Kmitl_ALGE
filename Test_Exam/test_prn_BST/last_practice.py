
class Node:
    def __init__(self, data): 
        self.data = int(data)  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.data) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    #edit insert to fit with ex4
    def insert(self, val):  
        if(self.root==None):
            self.root = Node(val)
            return self.root
        cur = self.root
        while(True):
            if(val <= cur.data):
                if(cur.left==None):
                    cur.left = Node(val)
                    break
                cur = cur.left
            elif(val > cur.data):
                if(cur.right == None):
                    cur.right = Node(val)
                    break
                cur = cur.right

        return self.root
    def delete(self,r : Node, data):
        #code here
        if(r == None):
            return
        
        if(data < r.data):
            r.left = self.delete(r.left,data)
        elif(data > r.data):
            r.right = self.delete(r.right,data)
        else:
            if(r.left==None):
                temp = r.right
                r = None
                return temp
            elif(r.right == None):
                temp = r.left
                r = None
                return temp
            else:
                minVal_node = self.getMinVal_node(r.right)
                r.data = minVal_node.data
                r.right = self.delete(r.right,minVal_node.data)
        return r

    def getMinVal_node(self,r:Node):
        cur = r
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
for item in data:
    order = item.split()[0]
    val = item.split()[1]
    if(order=="d"):
        print("delete "+str(val))
        tree.root = tree.delete(tree.root,int(val))
        printTree90(tree.root)
        continue
    if(order=="i"):
        tree.insert(int(val))
        printTree90(tree.root)
        continue


#i 3,i 2,i 4
#i 3,i 2,i 6,i 1,i 3,i 5,i 4