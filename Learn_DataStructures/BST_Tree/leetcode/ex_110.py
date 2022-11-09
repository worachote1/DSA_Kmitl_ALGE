# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) :
        return self.helper(root)

    def helper(self,root : TreeNode):
        if(root == None):
            return True
        a = self.findHeight(root.left,0)
        b = self.findHeight(root.right,0)

        return abs(a-b)<=1 and self.helper(root.left) and self.helper(root.right)
    def findHeight(self,root : TreeNode,h):
        if(root==None):
            return h-1
        left_h = self.findHeight(root.left,h+1)
        right_h = self.findHeight(root.right,h+1)

        return max(left_h,right_h)
        