
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
        #code here
        if(self.root == None):
            self.root = Node(val)
            print("insert "+str(val))
            return
        cur = self.root
        while(True):
            if(val <= cur.data):
                if(cur.left==None):
                    cur.left = Node(val)
                    print("insert "+str(val))
                    return
                cur = cur.left
                continue
            if(val > cur.data):
                if(cur.right==None):
                    cur.right = Node(val)
                    print("insert "+str(val))
                    return
                cur = cur.right
                continue
           
    def delete(self,r, data):
        #code here

        if(r==None):
            print("Error! Not Found DATA")
            return

        if(data != r.data):
            if(data < r.data):
                r.left = self.delete(r.left,data)
            elif(data > r.data):
                r.right = self.delete(r.right,data)
        
        elif(data == r.data):
            #if have only one child or no child
            
            #have only left child
            if(r.left==None):
                temp = r.right
                r = None
                return temp
            elif(r.right==None):
                temp = r.left
                r = None
                return temp

            # Node with two children: 
            # Get the inorder successor
            # (smallest in the right subtree)
            temp = self.getMinValue_node(r.right)
            r.data = temp.data
            r.right = self.delete(r.right,temp.data)

        return r

    def getMinValue_node(self,r):
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

