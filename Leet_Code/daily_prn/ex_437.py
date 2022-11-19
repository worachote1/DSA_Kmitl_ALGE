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
     
        return self.helper(root,targetSum,data,0)

    def helper(self,root : TreeNode, targetSum : int,data : dict,sumNum : int):
        if(root==None):
            return 0
        
        sumNum += root.val
        data[sumNum]=1+data.get(sumNum,0)

        res = data.get(sumNum-targetSum,0)
        res += self.helper(root.left,targetSum,data,sumNum) + self.helper(root.right,targetSum,data,sumNum)
        data[sumNum] -= 1 
        return res

