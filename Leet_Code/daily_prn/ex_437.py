# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) :
        data = {}
        data[0]=1

    def helper(self,root : TreeNode, targetSum : int):
