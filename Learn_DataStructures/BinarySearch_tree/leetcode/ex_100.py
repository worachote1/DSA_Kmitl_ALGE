#Ex 100 Same Tree
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode):
        return self.helper(p,q)

    def helper(self,root_p,root_q):

        if(root_p == root_q == None):
            return True
        
        elif(root_p != None or root_q != None):
            if(root_p == None):
                return False
            elif(root_q == None):
                return False
            elif(root_p.val != root_q.val):
                return False

        return self.helper(root_p.left,root_q.left) and self.helper(root_p.right,root_q.right)
        