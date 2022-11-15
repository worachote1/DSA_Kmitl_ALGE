# Ex 113. Path Sum II
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int):
        res = []
        #get array path sum    
        self.helper(root,res,[],targetSum)
        return res

    def helper(self,root : TreeNode,res : list , sub_res : list,targetSum : int):
        if(root == None):
            return
        targetSum -= root.val
        sub_res.append(root.val)
        if(targetSum == 0 and root.left == None and root.right == None):
            res.append(sub_res)
            return
        subLeft = sub_res.copy()
        subRight = sub_res.copy()
        self.helper(root.left,res,subLeft,targetSum)
        self.helper(root.right,res,subRight,targetSum)