# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) :
        return self.helper(root,float('-inf'),float('inf'))

    def helper(self,root : TreeNode,minBorder,maxBorder):
        if(root == None):
            return True

        return (root.val<maxBorder and root.val>=minBorder) and self.helper(root.left,minBorder,root.val) and self.helper(root.right,root.val,maxBorder)
