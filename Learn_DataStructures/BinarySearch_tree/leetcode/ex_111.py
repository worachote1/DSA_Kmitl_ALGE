#Ex 111 Minimum Depth of Binary Tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: TreeNode) :
        return self.helper(root)

    def helper(self,root : TreeNode):
        if(root== None):
            return 0

        if(root.left == None and root.right == None):
            return 1
        elif(root.left == None): 
            return self.helper(root.right)+1
        elif(root.right == None):
            return self.helper(root.left)+1

        return min(self.helper(root.left),self.helper(root.right))+1
        