#test delete inorder
class Node:
    def __init__(self,data) :
        self.data = int(data)
        self.left = None
        self.right = None
    def __str__(self) :
        return str(self.data)

class Binarysearchtree:
    def __init__(self): 
        self.root = None

    def insert(self, val):  
        if self.root==None:
            self.root = Node(val)
        else :
            intree = False
            temp = self.root
            while(not intree) :
                if temp.data<=val:
                    if temp.right==None:
                        temp.right = Node(val)
                        break
                    else :
                        temp = temp.right
                elif temp.data>val:
                    if temp.left==None:
                        temp.left = Node(val)
                        break
                    else :
                        temp = temp.left
        return self.root   
    
    def getMinVal(self,r):
        cur = r
        while(cur.left != None):
            cur = cur.left
        return cur
    def delete(self,r, data):
        if(r==None):
            print("Error! Not Found DATA")
            return
        
        if(data != r.data):
            if data > r.data:
                r.right = self.delete(r.right, data)
            elif data < r.data:
                r.left = self.delete(r.left, data)
        elif(data == r.data):
            if(r.left == None):
                r = r.right
                return r
            elif(r.right == None):
                r = r.left
                return r
            
            #remove node with 2 child
            else:
                temp = self.getMinVal(r.right)
                r.data = temp.data
                r.right = self.delete(r.right,temp.data)
        
        return r
    
    def delete2(self,r,data):
        if r == None :
            print('Error! Not Found DATA')
            return
        if r.data!=data:
            if r.data<=data:
                r.right = self.delete2(r.right, data)
            elif r.data>data:
                r.left = self.delete2(r.left, data)
        else:
            if r.right == None:
                r = r.left
                return r
            elif r.left == None:
                r = r.right
                return r
            else :
                temp = r.right
                while temp.left!=None :
                    temp = temp.left
                r.data = temp.data
                r.right = self.delete2(r.right,temp.data)
        return r 

def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)

#i 8,i 7,d 1,i 3,i 1,i 2,i 6,i 9,d 8,d 9,d 7,d 1,d 6,d 3,d 2
tree = Binarysearchtree()
data = input("Enter Input : ").split(",")
for i in range (len(data)):
    t = data[i].split()
    if t[0]=='i':
        print('insert '+str(t[1]))
        tree.insert(int(t[1]))
        printTree90(tree.root)
    elif t[0]=='d':
        print('delete '+str(t[1]))
        tree.root = tree.delete(tree.root,int(t[1]))
        printTree90(tree.root)

