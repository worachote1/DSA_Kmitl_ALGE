# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) :
        return self.helper(root,float('-inf'),float('inf'))

    def helper(self,root : TreeNode,minVal,maxVal):
        if(root == None):
            return True

        if(not (root.val > minVal and root.val < maxVal)):
            return False        

        return self.helper(root.left,minVal,root.val) and self.helper(root.right,root.val,maxVal)