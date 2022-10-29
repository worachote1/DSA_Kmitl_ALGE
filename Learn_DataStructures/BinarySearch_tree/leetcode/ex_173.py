# Ex 173. Binary Search Tree Iterator

# Definition for a binary tree node.
class Queue:
    def __init__(self):
        self.q = []
    def isEmpty(self):
        return len(self.q)==0
    def Dequeue(self):
        return self.q.pop(0)
    def Enqueue(self,data):
        self.q.append(data)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.root = root;
        self.BST_queue = self.getALL_inorder()        
    
    def getALL_inorder(self):
        q = Queue()
        self.helper(q,self.root)
        return q

    def helper(self,q,root):
        if(root == None):
            return
        self.helper(q,root.left)
        q.Enqueue(root.val)
        self.helper(q,root.right)

    def next(self) :
        return self.BST_queue.Dequeue()

    def hasNext(self) :
        return not self.BST_queue.isEmpty()