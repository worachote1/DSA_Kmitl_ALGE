class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Queue :
    def __init__(self) :
        self.q = []
    def Enqueue(self,val):
        self.q.append(val)
    def Dequeue(self):
        return self.q.pop(0)
    def isEmpty(self):
        return len(self.q)==0
    def size(self):
        return len(self.q)
    
class Solution:
    def levelOrderBottom(self, root : TreeNode) :
        if(root == None):
            return []
        data = Queue()
        data.Enqueue(root)
        res = [[root.val]]
        while(not data.isEmpty()):
            n = data.size()
            k = []
            for i in range(n):
                x = data.Dequeue()
                if(x.left != None):
                    data.Enqueue(x.left)
                    k.append(x.left.val)
                if(x.right != None):
                    data.Enqueue(x.right)
                    k.append(x.right.val)
            if(len(k) > 0):
                res.append(k)
        return res[::-1]