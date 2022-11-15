class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) :
        sumNum = 0
        return self.helper(root,targetSum,sumNum)

    def helper(self,root : TreeNode,targetSum : int,sumNum : int):
        if(root == None):
            return False
        sumNum += root.val
        if(root.left == None and root.right == None):
            return sumNum == targetSum
        return self.helper(root.left,targetSum,sumNum) or self.helper(root.right,targetSum,sumNum) 

