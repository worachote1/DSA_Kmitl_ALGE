class Queue:
    def __init__(self):
        self.q = []
    def Enqueue(self,i):
        self.q.append(i)
    def dequeue(self):
        return self.q.pop(0)
    def isEmpty(self):
        return len(self.q) == 0
    def size(self):
        return len(self.q)
    def show(self):
        return self.q.copy()

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countNodes(self, root: TreeNode) :
        return 0 if root == None else self.helper(root) 

    def helper(self,root : TreeNode):
        q = Queue()
        count = 0
        q.Enqueue(root)
        while(not q.isEmpty()):
            r = q.dequeue()
            count += 1
            if(r.left != None):
                q.Enqueue(r.left)
            if(r.right != None):
                q.Enqueue(r.right)
        
        return count