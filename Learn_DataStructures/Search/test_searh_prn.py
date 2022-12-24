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
             
    def delete(self,r, data):
        if r == None :
            print('Error! Not Found DATA')
            return
        if r.data!=data:
            if r.data<=data:
                r.right = self.delete(r.right, data)
            elif r.data>data:
                r.left = self.delete(r.left, data)
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
                r.right = self.delete(r.right,temp.data)
        return r 
