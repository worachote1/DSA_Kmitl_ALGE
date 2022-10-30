#Ex 101 Symmetric Tree

#Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) :
        return self.helper(root.left,root.right)

    def helper(self,root_a,root_b):
        if(root_a == root_b == None):
            return True
        
        if(root_a == None or root_b == None):
            return False

        if(root_a.val != root_b.val):
            return False

        return self.helper(root_a.left,root_b.right) and self.helper(root_a.right,root_b.left)
