# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) :
        self.numOfpath = 0
        self.helper(root,targetSum)
        return self.numOfpath

    def helper(self,root : TreeNode, targetSum : int):
        if(root == None):
            return 
        targetSum -= root.val
        if(targetSum == 0):
            self.numOfpath+=1

        self.helper(root.left,targetSum)
        self.helper(root.right,targetSum)
